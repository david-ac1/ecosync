import os
import base64
from anthropic import Anthropic
import json

class ParsingService:
    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        # Initialize Anthropic client if a real key is provided
        self.client = Anthropic(api_key=self.api_key) if self.api_key and "your_anthropic_key" not in self.api_key else None

    def parse_receipt(self, file_bytes: bytes, media_type: str = "image/jpeg"):
        if not self.client:
            print("No real Anthropic key. Falling back to mock receipt parsing.")
            return {
                "title": "Mock Receipt Asset",
                "category": "Tech",
                "bought_year": "2024",
                "resale_value": "$199.00"
            }
            
        try:
            base64_image = base64.b64encode(file_bytes).decode('utf-8')
            prompt = """
            Analyze this receipt. Extract the most valuable standalone item.
            Format exactly as JSON with these keys: 
            - title: The name of the item
            - category: 'Tech', 'Apparel', 'Auto', or 'Home'
            - bought_year: (extract the year)
            - resale_value: (estimate current value, format like $100.00)
            Return ONLY valid JSON. Nothing else.
            """
            
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": media_type,
                                    "data": base64_image
                                }
                            },
                            {
                                "type": "text",
                                "text": prompt
                            }
                        ]
                    }
                ]
            )
            
            content = response.content[0].text
            # Clean JSON block if present
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0]
            elif "```" in content:
                content = content.split("```")[1].split("```")[0]
                
            return json.loads(content.strip())
        except Exception as e:
            print(f"Error parsing receipt: {e}")
            return {
                "title": "Failed to Parse: Unknown Item",
                "category": "Unknown",
                "bought_year": "2024",
                "resale_value": "$0.00"
            }

parsing_service = ParsingService()

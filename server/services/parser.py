import os
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

class ReceiptParser:
    def __init__(self):
        self.llm = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0)
        
    async def parse(self, raw_text: str):
        prompt = ChatPromptTemplate.from_template("""
        You are an expert at extracting product information from digital receipts and order confirmations.
        Extract the following information from the text provided:
        1. Product Name
        2. Category (Apparel, Tech, Home, Other)
        3. Purchase Price
        4. Purchase Date (Year only)
        
        Return the information as a structured JSON object.
        
        Input Text:
        {text}
        """)
        
        chain = prompt | self.llm
        # For simulation purposes in Phase 1, we might return mock structured data if no API key is present
        if not os.getenv("ANTHROPIC_API_KEY"):
            return {
                "title": "New Detected Item",
                "category": "Other",
                "bought_year": "2024",
                "resale_value": "$0",
                "health_score": 100
            }
            
        response = await chain.ainvoke({"text": raw_text})
        return response.content

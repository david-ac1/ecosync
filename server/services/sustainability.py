from datetime import datetime

class SHIService:
    def __init__(self):
        # Base LCA impact constants (kg CO2 offset potential)
        self.lca_impacts = {
            "Apparel": 12,
            "Tech": 85,
            "Home": 25,
            "Other": 10
        }
        
    def calculate_shi(self, category: str, bought_year: str, resale_value: str):
        """
        Calculate Sustainability Health Index (0-100)
        Logic: 
        1. Physical Decay: -15% per year for Tech, -10% for others.
        2. Circularity Delta: Bonus if resale value is > 50% of original (simulated).
        """
        current_year = datetime.now().year
        age = current_year - int(bought_year)
        
        # Base health starts at 100
        health = 100
        
        # Physical Decay
        decay_rate = 15 if category == "Tech" else 10
        health -= (age * decay_rate)
        
        # Ensure health doesn't drop below 5
        health = max(health, 5)
        
        # CO2 Offset potential
        co2_offset = self.lca_impacts.get(category, 10) * (health / 100)
        
        return int(health), f"{co2_offset:.1f}kg CO2"

shi_service = SHIService()

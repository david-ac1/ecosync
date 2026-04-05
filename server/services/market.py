import random

class MarketService:
    def __init__(self):
        # Mock floor prices for known items
        self.market_data = {
            "Arc'teryx Alpha SV": {"min": 220, "max": 280, "trend": "Stable"},
            "iPad Pro 12.9\" M2": {"min": 640, "max": 720, "trend": "Dropping"},
            "Uniqlo Down Parka": {"min": 90, "max": 130, "trend": "Stable"},
            "iPhone 13": {"min": 380, "max": 450, "trend": "Rising"},
        }
        
    def get_floor_price(self, item_title: str):
        data = self.market_data.get(item_title, {"min": 50, "max": 100, "trend": "Unknown"})
        # Add a bit of randomness to simulate live market fluctuations
        fluctuation = random.uniform(-0.02, 0.02)
        price = data["max"] * (1 + fluctuation)
        return f"${price:.2f}", data["trend"]

market_service = MarketService()

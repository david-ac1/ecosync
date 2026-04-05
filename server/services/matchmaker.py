class MatchmakerService:
    def __init__(self):
        pass
        
    def get_recommendation(self, category: str, health: int, trend: str, prediction: str):
        """
        Agentic Decision Tree for Redistribution
        """
        if health < 30:
            return "DIGITAL RECYCLE", "RECYCLE"
        
        if category == "Tech":
            if "SELL NOW" in (prediction or ""):
                return "BACK MARKET TRADE-IN", "TRADE-IN"
            return "SWAPPA LISTING", "LIST FOR SALE"
            
        if category == "Apparel":
            if health > 80:
                return "VESTIAIRE COLLECTIVE", "LIST FOR SALE"
            return "DEPOP CURATION", "LIST FOR SALE"
            
        return "LOCAL DONATION", "DONATE"

matchmaker_service = MatchmakerService()

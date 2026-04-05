from datetime import datetime

class PredictorEngine:
    def __init__(self):
        pass
        
    def predict_peak_window(self, item_title: str, category: str, bought_year: str):
        # Tech items have more predictable peak windows (e.g. before new releases)
        if category == "Tech":
            # Simple logic: Peak window is usually 6-9 months after launch or before next year's model
            current_year = datetime.now().year
            years_owned = current_year - int(bought_year)
            
            if years_owned <= 1:
                return "SELL NOW: 92% Peak Value"
            elif years_owned == 2:
                return "HOLD: 45% Depreciation"
            else:
                return "RECYCLE: Low Utility"
        
        return None

predictor_engine = PredictorEngine()

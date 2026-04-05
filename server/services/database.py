import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class DatabaseService:
    def __init__(self):
        url: str = os.getenv("SUPABASE_URL")
        key: str = os.getenv("SUPABASE_KEY")
        
        if not url or not key or "your_supabase" in url:
            self.client = None
            print("Supabase credentials not found. Falling back to mock data.")
        else:
            self.client: Client = create_client(url, key)
            
    def get_inventory(self):
        if not self.client:
            return None
        
        try:
            response = self.client.table("inventory").select("*").execute()
            return response.data
        except Exception as e:
            print(f"Error fetching from Supabase: {e}")
            return None
            
    def add_item(self, item_data: dict):
        if not self.client:
            return None
            
        try:
            response = self.client.table("inventory").insert(item_data).execute()
            return response.data
        except Exception as e:
            print(f"Error adding to Supabase: {e}")
            return None

database_service = DatabaseService()

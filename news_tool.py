import requests
from dotenv import load_dotenv
import os
load_dotenv()

def get_latest_news(topic: str) -> str:
    api_key=os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q=bitcoin&apiKey={api_key}" 
    
    result = requests.get(url)

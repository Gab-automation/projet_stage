from smolagents import CodeAgent, OpenAIServerModel, MultiStepAgent, Tool
from smolagents import 
import tools
import requests
import wikipediaapi
from dotenv import load_dotenv
import os
load_dotenv()

import wikipediaapi

def search_wikipedia(topic: str) -> str:
    wiki = wikipediaapi.Wikipedia(
        language='fr',
        user_agent='MyWikipediaBot/1.0 (https://github.com/monutilisateur/monbot; contact: email@example.com)'
    )
    page = wiki.page(topic)

    if not page.exists():
        return f"La page '{topic}' n'a pas été trouvée sur Wikipédia."

    summary = page.summary.strip()
    paragraphs = summary.split('\n')
    top_paragraphs = "\n\n".join(paragraphs[:3])

    return top_paragraphs

search_wikipedia("topic")

wikipedia_tool=search_wikipedia

def get_latest_news(topic: str) -> str:
    api_key=os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q=stablecoin&apiKey={api_key}" 
    
    return requests.get(url)
topic = 'topic'
latest_new = get_latest_news(topic)
new_content=latest_new.json()
articles = new_content.get('articles')
articles
articles = new_content.get('articles')
responses = []
limit = 0
nb_range = 3
for i in range(nb_range):
    article = articles[i]
    article_row = {
        "sources": article.get('source').get('name'),
        "title": article.get('title'),
        "date": article.get('publishedAt'),
        "description": article.get('description')
    }
    responses.append(article_row)
responses

news_tool=get_latest_news

planner_prompt="Tu es un planificateur expert. Ta mission est de décomposer une question complexe et d'utiliser les outils à ta disposition pour collecter les informations nécessaires."
PlannerAgent = MultiStepAgent(
    model=OpenAIServerModel,
    planning_interval=(1),
    system_prompt=planner_prompt,
    tools=[wikipedia_tool, news_tool]
)
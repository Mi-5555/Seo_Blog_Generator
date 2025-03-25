import requests
from bs4 import BeautifulSoup

class ResearchAgent:
    def fetch_trending_hr_topics(self):
        """Fetches trending HR topics from a sample HR blog (or use Google Trends API)."""
        url = "https://www.shrm.org/hr-today/news/hr-news"
        response = requests.get(url)
        
        if response.status_code != 200:
            return ["HR Automation", "Employee Well-being", "Remote Work Trends"]
        
        soup = BeautifulSoup(response.text, "html.parser")
        topics = [item.text.strip() for item in soup.find_all("h3")][:5]  # Extract top 5 topics
        return topics

if __name__ == "__main__":
    agent = ResearchAgent()
    print(agent.fetch_trending_hr_topics())

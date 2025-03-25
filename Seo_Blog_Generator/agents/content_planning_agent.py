class ContentPlanningAgent:
    def generate_outline(self, topic):
        """Creates a structured outline for the blog post."""
        return {
            "title": f"{topic}: A Complete Guide",
            "sections": [
                "Introduction",
                f"What is {topic}?",
                "Benefits & Challenges",
                "Implementation Strategies",
                "Best Practices",
                "Future Trends",
                "Conclusion"
            ]
        }

if __name__ == "__main__":
    agent = ContentPlanningAgent()
    print(agent.generate_outline("HR Automation"))

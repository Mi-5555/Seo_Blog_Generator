import openai

class ContentGenerationAgent:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_content(self, outline):
        """Generates blog content based on the outline."""
        blog_content = f"# {outline['title']}\n\n"
        for section in outline["sections"]:
            prompt = f"Write a detailed section on '{section}' for an HR blog."
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            blog_content += f"## {section}\n{response['choices'][0]['message']['content']}\n\n"
        return blog_content

if __name__ == "__main__":
    api_key = "your_openai_api_key"
    agent = ContentGenerationAgent(api_key)
    outline = {
        "title": "HR Automation: A Complete Guide",
        "sections": ["Introduction", "What is HR Automation?", "Conclusion"]
    }
    print(agent.generate_content(outline))

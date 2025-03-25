from agents.research_agent import ResearchAgent
from agents.content_planning_agent import ContentPlanningAgent
from agents.content_generation_agent import ContentGenerationAgent
from agents.seo_optimization_agent import SEOOptimizationAgent
from agents.review_agent import ReviewAgent
from utils.helpers import save_as_markdown, save_as_html, save_as_pdf

api_key = "your_openai_api_key"

# Step 1: Research trending HR topics
research_agent = ResearchAgent()
topics = research_agent.fetch_trending_hr_topics()
selected_topic = topics[0]  # Pick first topic

# Step 2: Plan content
planning_agent = ContentPlanningAgent()
outline = planning_agent.generate_outline(selected_topic)

# Step 3: Generate content
generation_agent = ContentGenerationAgent(api_key)
blog_content = generation_agent.generate_content(outline)

# Step 4: Optimize content
seo_agent = SEOOptimizationAgent()
seo_report = seo_agent.optimize_content(blog_content, selected_topic)

# Step 5: Review content
review_agent = ReviewAgent()
review_report = review_agent.review_content(blog_content)

# Step 6: Save outputs
save_as_markdown(blog_content)
save_as_html(blog_content)
save_as_pdf(blog_content)

print("Blog Generated Successfully!")
print(f"SEO Report: {seo_report}")
print(f"Review Report: {review_report}")

import nltk
from nltk.tokenize import sent_tokenize
from textstat import text_standard

class ReviewAgent:
    def review_content(self, content):
        """Performs readability check and basic grammar analysis."""
        sentences = sent_tokenize(content)
        readability_level = text_standard(content)

        return {
            "Sentence Count": len(sentences),
            "Readability Level": readability_level
        }

if __name__ == "__main__":
    agent = ReviewAgent()
    sample_text = "HR Automation is the future. It optimizes HR tasks."
    print(agent.review_content(sample_text))

"""
Web Browsing Agent
------------------
This program demonstrates an AI agent
that browses web pages to collect information.

Author: AI Course
"""

class WebBrowser:
    def fetch(self, url):
        # Simulated webpage content
        pages = {
            "https://ai.com/ml": "Machine learning enables systems to learn from data.",
            "https://ai.com/dl": "Deep learning uses neural networks.",
            "https://ai.com/ai": "Artificial intelligence is the science of intelligent machines."
        }
        return pages.get(url, "404 Page Not Found")


class WebBrowsingAgent:
    def __init__(self):
        self.browser = WebBrowser()

    def decide_url(self, topic):
        if "machine learning" in topic:
            return "https://ai.com/ml"
        if "deep learning" in topic:
            return "https://ai.com/dl"
        return "https://ai.com/ai"

    def browse(self, topic):
        url = self.decide_url(topic)
        print("Browsing:", url)
        content = self.browser.fetch(url)
        return content

    def run(self, topic):
        print("Topic:", topic)
        page_content = self.browse(topic)
        print("Extracted Content:")
        print(page_content)


def main():
    print("WEB-BROWSING AI AGENT")
    print("----------------------")

    agent = WebBrowsingAgent()
    agent.run("machine learning")


if __name__ == "__main__":
    main()

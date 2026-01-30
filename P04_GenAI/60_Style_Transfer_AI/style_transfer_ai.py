"""
Style Transfer AI (Conceptual)
------------------------------
This program demonstrates the idea of
neural style transfer: combining
content and style.

Author: AI Course
"""

import random


class StyleTransferAI:
    def __init__(self):
        self.styles = [
            "Van Gogh painting style",
            "Watercolor art style",
            "Pencil sketch style",
            "Oil painting style"
        ]

    def extract_content(self, image):
        # Simulate content extraction
        return "content structure of the image"

    def extract_style(self, style_image):
        # Simulate style extraction
        return random.choice(self.styles)

    def generate_image(self, content, style):
        return f"Image with {content} painted in {style}"

    def transfer(self, content_image, style_image):
        content = self.extract_content(content_image)
        style = self.extract_style(style_image)
        return self.generate_image(content, style)


def main():
    print("STYLE TRANSFER AI")
    print("------------------")

    model = StyleTransferAI()

    content_image = "photo.jpg"
    style_image = "art.jpg"

    result = model.transfer(content_image, style_image)

    print("\nGenerated Image Description:")
    print(result)


if __name__ == "__main__":
    main()

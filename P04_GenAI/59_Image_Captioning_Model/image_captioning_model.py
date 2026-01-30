"""
Image Captioning Model (Conceptual)
----------------------------------
This program demonstrates how images
are converted into text captions.

Author: AI Course
"""

import random


class ImageCaptioningModel:
    def __init__(self):
        # Pretend visual features detected from an image
        self.visual_features = [
            "a dog", "a cat", "a person",
            "a car", "a bicycle", "a ball"
        ]

        # Caption templates
        self.templates = [
            "This image shows {}.",
            "There is {} in the picture.",
            "The photo contains {}."
        ]

    def extract_features(self, image):
        """
        Simulate CNN feature extraction.
        """
        return random.choice(self.visual_features)

    def generate_caption(self, image):
        feature = self.extract_features(image)
        template = random.choice(self.templates)
        return template.format(feature)


def main():
    print("IMAGE CAPTIONING MODEL")
    print("-----------------------")

    model = ImageCaptioningModel()

    fake_image = "image.jpg"  # placeholder
    caption = model.generate_caption(fake_image)

    print("\nGenerated Caption:")
    print(caption)


if __name__ == "__main__":
    main()

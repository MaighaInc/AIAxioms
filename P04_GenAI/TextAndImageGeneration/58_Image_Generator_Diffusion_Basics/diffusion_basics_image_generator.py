"""
Diffusion Image Generator (Conceptual)
--------------------------------------
This program demonstrates the idea of
diffusion: removing noise step by step
to generate an image.

Author: AI Course
"""

import numpy as np


class DiffusionModel:
    def __init__(self, steps=10):
        self.steps = steps

    def add_noise(self, image):
        noise = np.random.randn(*image.shape)
        return image + noise

    def denoise(self, noisy_image):
        # Simple smoothing to simulate denoising
        return noisy_image * 0.9

    def generate(self):
        # Start from pure noise
        image = np.random.randn(8, 8)

        print("Starting from noise...\n")

        for step in range(self.steps):
            image = self.denoise(image)
            print(f"Step {step + 1}: Image becoming clearer")

        return image


def main():
    print("DIFFUSION IMAGE GENERATOR (BASICS)")
    print("----------------------------------")

    diffusion = DiffusionModel(steps=10)
    final_image = diffusion.generate()

    print("\nFinal Generated Image (Matrix):")
    print(final_image)


if __name__ == "__main__":
    main()

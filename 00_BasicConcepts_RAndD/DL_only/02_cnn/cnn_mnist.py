import torch
import torch.nn as nn

# Random image batch (like MNIST 28x28)
x = torch.randn(4, 1, 28, 28)

model = nn.Sequential(
    nn.Conv2d(1, 4, kernel_size=3),
    nn.ReLU(),
    nn.Flatten(),
    nn.Linear(4*26*26, 10)
)

print("CNN output shape:", model(x).shape)

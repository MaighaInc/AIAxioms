import torch
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(10, 3),
    nn.ReLU(),
    nn.Linear(3, 10)
)

x = torch.randn(5, 10)
recon = model(x)

print(recon.shape)

import torch
import torch.nn as nn

G = nn.Sequential(nn.Linear(10, 20), nn.ReLU(), nn.Linear(20, 10))
D = nn.Sequential(nn.Linear(10, 20), nn.ReLU(), nn.Linear(20, 1), nn.Sigmoid())

noise = torch.randn(5, 10)
fake = G(noise)
decision = D(fake)

print(decision.shape)

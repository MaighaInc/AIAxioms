import torch
import torch.nn as nn

class VAE(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 5)
        self.fc2 = nn.Linear(5, 10)

    def forward(self, x):
        z = torch.relu(self.fc1(x))
        return self.fc2(z)

vae = VAE()
print(vae(torch.randn(2, 10)).shape)

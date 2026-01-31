import torch
import torch.nn.functional as F

q = torch.randn(1, 5)
k = torch.randn(1, 5)
v = torch.randn(1, 5)

weights = F.softmax(q @ k.T, dim=-1)
output = weights @ v

print(output)

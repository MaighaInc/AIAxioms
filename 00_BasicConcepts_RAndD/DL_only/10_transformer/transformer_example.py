import torch
import torch.nn as nn

layer = nn.TransformerEncoderLayer(d_model=8, nhead=2)
encoder = nn.TransformerEncoder(layer, num_layers=2)

x = torch.randn(5, 1, 8)
out = encoder(x)

print(out.shape)

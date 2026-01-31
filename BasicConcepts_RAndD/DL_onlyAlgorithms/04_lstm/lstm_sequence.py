import torch
import torch.nn as nn

lstm = nn.LSTM(input_size=1, hidden_size=5, batch_first=True)

x = torch.randn(1, 10, 1)
output, _ = lstm(x)

print(output.shape)

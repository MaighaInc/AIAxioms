import torch
import torch.nn as nn

rnn = nn.RNN(input_size=1, hidden_size=5, batch_first=True)

x = torch.randn(1, 10, 1)  # batch, time, features
output, hidden = rnn(x)

print(output.shape)

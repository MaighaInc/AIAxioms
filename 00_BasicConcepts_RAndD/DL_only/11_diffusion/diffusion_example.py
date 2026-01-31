import torch

x = torch.randn(1, 10)
noise = torch.randn_like(x)

noisy = x + noise * 0.1
denoised = noisy - noise * 0.1

print(denoised.shape)

import numpy as np


def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / np.sum(e_x)


def layer_norm(x, eps=1e-6):
    mean = np.mean(x)
    std = np.std(x)
    return (x - mean) / (std + eps)


def masked_attention(Q, K, V):
    scores = np.dot(Q, K.T)              # ✅ FIXED
    mask = np.triu(np.ones_like(scores), k=1) * -1e9
    scores = scores + mask
    weights = softmax(scores)
    return np.dot(weights, V)


def feed_forward(x, W1, W2):
    return np.dot(np.maximum(0, np.dot(x, W1)), W2)


def main():
    print("MINI TRANSFORMER DECODER")
    print("-------------------------")

    X = np.array([
        [0.2, 0.1, 0.4, 0.3],
        [0.1, 0.3, 0.2, 0.4],
        [0.4, 0.2, 0.1, 0.3]
    ])

    encoder_output = np.array([
        [0.6, 0.1, 0.2, 0.1],
        [0.5, 0.2, 0.2, 0.1],
        [0.4, 0.3, 0.2, 0.1]
    ])

    # Weights
    Wq = np.random.randn(4, 4)
    Wk = np.random.randn(4, 4)
    Wv = np.random.randn(4, 4)

    Wq_enc = np.random.randn(4, 4)
    Wk_enc = np.random.randn(4, 4)
    Wv_enc = np.random.randn(4, 4)

    W1 = np.random.randn(4, 8)
    W2 = np.random.randn(8, 4)

    outputs = []

    for x in X:
        # Self-Attention
        Q = np.dot(x, Wq)
        K = np.dot(X, Wk)
        V = np.dot(X, Wv)

        self_attn = masked_attention(Q, K, V)
        x1 = layer_norm(x + self_attn)

        # Encoder-Decoder Attention
        Q_enc = np.dot(x1, Wq_enc)
        K_enc = np.dot(encoder_output, Wk_enc)
        V_enc = np.dot(encoder_output, Wv_enc)

        scores_enc = np.dot(Q_enc, K_enc.T)   # ✅ FIXED
        weights_enc = softmax(scores_enc)
        enc_attn = np.dot(weights_enc, V_enc)

        x2 = layer_norm(x1 + enc_attn)

        # Feed Forward
        ff_out = feed_forward(x2, W1, W2)
        decoder_out = layer_norm(x2 + ff_out)

        outputs.append(decoder_out)

    outputs = np.array(outputs)

    print("\nDecoder Output:")
    print(outputs)


if __name__ == "__main__":
    main()

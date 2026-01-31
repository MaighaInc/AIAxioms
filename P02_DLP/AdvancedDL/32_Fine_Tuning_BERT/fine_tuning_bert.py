"""
Fine-Tuning BERT for Text Classification
----------------------------------------
This program fine-tunes a pretrained BERT model
for sentiment analysis.

Author: AI Course
"""

import torch
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import Trainer, TrainingArguments


def main():
    print("FINE-TUNING BERT")

    # Sample dataset
    texts = [
        "I love this product",
        "This is the worst experience",
        "Amazing quality and great service",
        "I hate this so much",
        "Very happy with the purchase",
        "Terrible and disappointing"
    ]

    labels = [1, 0, 1, 0, 1, 0]  # 1 = Positive, 0 = Negative

    # Load tokenizer
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

    # Tokenize data
    encodings = tokenizer(
        texts,
        truncation=True,
        padding=True,
        return_tensors="pt"
    )

    class SentimentDataset(torch.utils.data.Dataset):
        def __init__(self, encodings, labels):
            self.encodings = encodings
            self.labels = labels

        def __getitem__(self, idx):
            item = {key: val[idx] for key, val in self.encodings.items()}
            item["labels"] = torch.tensor(self.labels[idx])
            return item

        def __len__(self):
            return len(self.labels)

    dataset = SentimentDataset(encodings, labels)

    # Load pretrained BERT model
    model = BertForSequenceClassification.from_pretrained(
        "bert-base-uncased",
        num_labels=2
    )

    # Training configuration
    training_args = TrainingArguments(
        output_dir="./results",
        num_train_epochs=3,
        per_device_train_batch_size=2,
        logging_dir="./logs",
        logging_steps=10
    )

    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset
    )

    # Train
    trainer.train()

    # Test prediction
    test_text = "I really enjoyed this experience"
    inputs = tokenizer(test_text, return_tensors="pt")
    outputs = model(**inputs)
    prediction = torch.argmax(outputs.logits, dim=1)

    print("\nTest sentence:", test_text)
    print("Predicted sentiment:", "Positive" if prediction.item() == 1 else "Negative")


if __name__ == "__main__":
    main()

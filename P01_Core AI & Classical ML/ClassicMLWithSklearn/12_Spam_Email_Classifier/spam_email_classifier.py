"""
Spam Email Classifier using Scikit-learn
----------------------------------------
This program classifies emails as Spam or Ham
using text vectorization and Naive Bayes.

Author: AI Course
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def main():
    print("SPAM EMAIL CLASSIFIER")
    print("----------------------")

    # Dataset
    emails = [
        "Win money now",
        "Limited offer win big",
        "Win a free prize now",
        "Meeting tomorrow at office",
        "Project discussion scheduled",
        "Let us plan the meeting"
    ]

    labels = [
        "Spam",
        "Spam",
        "Spam",
        "Ham",
        "Ham",
        "Ham"
    ]

    # Convert text to numerical features
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(emails)

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, labels, test_size=0.33, random_state=42
    )

    # Train model
    model = MultinomialNB()
    model.fit(X_train, y_train)

    # Predictions
    predictions = model.predict(X_test)

    # Evaluation
    print("\nAccuracy:", accuracy_score(y_test, predictions))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, predictions))
    print("\nClassification Report:\n", classification_report(y_test, predictions))

    # Predict new email
    new_email = ["Win free money now"]
    new_email_vector = vectorizer.transform(new_email)
    new_prediction = model.predict(new_email_vector)

    print("\nNew Email:", new_email[0])
    print("Prediction:", new_prediction[0])


if __name__ == "__main__":
    main()

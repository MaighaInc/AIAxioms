"""
K-Nearest Neighbors (From Scratch)
---------------------------------
This program classifies a point based on
distance to nearby data points.

Author: AI Course
"""

import math
from collections import Counter


class KNNClassifier:
    def __init__(self, k=3):
        self.k = k
        self.data = []

    def fit(self, data):
        """
        Stores the training data.
        data: list of tuples (features, label)
        """
        self.data = data

    def _euclidean_distance(self, point1, point2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

    def predict(self, point):
        """
        Predicts class for a given data point.
        """
        distances = []

        for features, label in self.data:
            dist = self._euclidean_distance(features, point)
            distances.append((dist, label))

        distances.sort(key=lambda x: x[0])
        nearest_labels = [label for _, label in distances[:self.k]]

        return Counter(nearest_labels).most_common(1)[0][0]


def main():
    print("K-NEAREST NEIGHBORS CLASSIFIER")
    print("------------------------------")

    # Training data
    training_data = [
        ([1, 2], "A"),
        ([2, 3], "A"),
        ([3, 3], "A"),
        ([6, 5], "B"),
        ([7, 7], "B"),
        ([8, 6], "B")
    ]

    knn = KNNClassifier(k=3)
    knn.fit(training_data)

    test_point = [2, 2]
    prediction = knn.predict(test_point)

    print("Test Point:", test_point)
    print("Predicted Class:", prediction)


if __name__ == "__main__":
    main()

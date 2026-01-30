"""
Decision Tree Classifier (From Scratch)
--------------------------------------
This program demonstrates how a simple decision tree
can make decisions using learned rules.

Author: AI Course
"""

def decision_tree_predict(age, income):
    """
    Predicts whether a person will buy a product.

    Parameters:
    age (int): Age of the customer
    income (int): Annual income

    Returns:
    str: 'Yes' or 'No'
    """

    # Root node
    if age < 30:
        return "No"

    # Second level
    else:
        if income >= 50000:
            return "Yes"
        else:
            return "No"


def main():
    print("DECISION TREE CLASSIFIER")
    print("-------------------------")

    # Sample data
    age = 35
    income = 60000

    print("Customer Age:", age)
    print("Customer Income:", income)

    prediction = decision_tree_predict(age, income)

    print("\nPrediction Result:", prediction)


if __name__ == "__main__":
    main()

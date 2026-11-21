import pandas as pd

from sklearn.model_selection import train_test_split

df = pd.DataFrame(
    {
        "hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "passed": [0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
    }
)


X = df[["hours"]]
y = df["passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

assert len(X_train) == 8
assert len(X_test) == 2
assert len(y_train) == 8
assert len(y_test) == 2

X_train_again, X_test_agian, _, _ = train_test_split(
    X, y, test_size=0.2, random_state=42
)
assert list(X_test["hours"]) == list(X_test_agian["hours"])

def accuracy(actual, predicted):
    correct = 0
    for a, p in zip(actual, predicted):
        if a == p:
            correct = correct + 1
    return correct / len(actual)

assert accuracy([1, 0, 1, 1], [1, 0, 0, 1]) == 0.75
assert accuracy([1, 1], [1, 1]) == 1.0
assert accuracy([1, 0], [0, 1]) == 0.0

print("all checks passed")
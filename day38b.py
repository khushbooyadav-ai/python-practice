import pandas as pd

from sklearn.model_selection import train_test_split

df = pd.DataFrame(
    {
        "age": [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115],
        "buys": [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    }
)

X = df[["age"]]
y = df["buys"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=7
)

assert len(X_train) == 15
assert len(X_test) == 5
assert len(y_train) == 15
assert len(y_test) == 5

X_train_again, X_test_again, _, _ = train_test_split(
    X, y, test_size=0.25, random_state=7
)
assert list(X_test["age"]) == list(X_test_again["age"])

def accuracy(actual, predicted):
    correct = 0
    for a, p in zip(actual, predicted):
        if a == p:
            correct = correct + 1
    return correct / len(actual)

assert accuracy([1, 0, 1, 1], [1, 0, 0, 1]) == 0.75
assert accuracy([1, 1], [1, 1]) == 1.0
assert accuracy([1, 0], [0, 1]) == 0.0
assert accuracy([1, 0], [1, 1]) == 0.5
assert accuracy([1, 1, 1, 1], [1, 1, 1, 1]) == 1.0
assert accuracy([1, 1], [0, 1]) == 0.5

share_buys = y.mean()
assert share_buys == 0.5

print("all checks passed")
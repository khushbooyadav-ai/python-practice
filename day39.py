import pandas as pd
from sklearn.linear_model import  LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.DataFrame(
    {
        "hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "passed": [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    }
)

X = df[["hours"]]
y = df["passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
assert len(predictions) == len(y_test)

correct = 0
for actual, predicted in zip(y_test, predictions):
    if actual == predicted:
        correct = correct + 1
score = correct / len(y_test)
assert 0.0 <= score <= 1.0
assert score == model.score(X_test, y_test) 

assert model.predict(pd.DataFrame({"hours": [1]}))[0] == 0
assert model.predict(pd.DataFrame({"hours": [12]}))[0] == 1
print("accuracy:", score)
print("all checks passed")
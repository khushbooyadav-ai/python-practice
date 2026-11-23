import pandas as pd

from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

df = pd.DataFrame(
    {
        "attendance": [40,45,50,55,60,65,70,75,80,85,90,95,42,58,68,78,88,98,52,72],
        "passed": [0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,0,1],
    }
)

X = df[["attendance"]]
y = df["passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=1
)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(df)
print(X_test["attendance"].tolist())
print(y_test.tolist())
print(predictions.tolist())
assert len(predictions) == len(y_test)

correct = 0
for actual, predicted in zip(y_test, predictions):
    if actual == predicted:
        correct = correct + 1
score = correct / len(y_test)
assert 0.0 <= score <= 1.0
assert score == model.score(X_test, y_test)

assert model.predict(pd.DataFrame({"attendance": [30]}))[0] == 0
assert model.predict(pd.DataFrame({"attendance": [99]}))[0] == 1
assert model.predict(pd.DataFrame({"attendance": [60]}))[0] == 0

assert model.predict(pd.DataFrame({"attendance": [75]}))[0] == 1

print("accuracy:", score)
print("all checks passed")
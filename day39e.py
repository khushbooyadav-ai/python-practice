import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.DataFrame(
    {
        "practice_hours": [1,2,3,4,5,6,7,8,9,10,11,12,1.5,3.5,5.5,7.5,9.5,11.5,2.5,6.5],
        "selected": [0,0,0,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,0,1],
    }
)

X = df[["practice_hours"]]
y = df["selected"]

wrong_counts = {}
for seed in range(10):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=seed
    )
    model = LogisticRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    wrong = [
        h
        for h, truth, guess in zip(X_test["practice_hours"], y_test, predictions)
        if truth != guess
    ]
    for h in wrong:
        wrong_counts[h] = wrong_counts.get(h, 0) + 1
        print("seed", seed, "wrong rows:", wrong)
    print(sorted(wrong_counts.items(), key=lambda item: item[1], reverse=True))
    print("total wrong:", sum(wrong_counts.values()))
    print(X_test["practice_hours"].tolist(), y_test.tolist(), predictions.tolist())
    print("seed", seed, "accuracy", model.score(X_test, y_test))
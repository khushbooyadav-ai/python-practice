import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.DataFrame( 
    {
        "attendance": [40,45,50,55,60,65,70,75,80,85,90,95,42,58,68,78,88,98,52,72],
        "passed": [0,0,0,0,1,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1],
    }
)

X = df[["attendance"]]
y = df["passed"]

for seed in range(10):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=seed
    )
    model = LogisticRegression()
    model.fit(X_train, y_train)
    print("seed", seed, "accuracy", model.score(X_test, y_test))
import pandas as pd

df = pd.DataFrame({"name": ["a", "b", "c"], "marks": [50, None, 90]})
print(df["marks"].isna().sum())
print(list(df[df["marks"].isna()]["name"]))
import pandas as pd

df = pd.DataFrame({"item": ["tea", "bus", "pen"], "amount": [20, 50, 10]})
ordered = df.sort_values("amount", ascending=False)
print(list(ordered["item"]))
print(ordered.iloc[0]["item"])

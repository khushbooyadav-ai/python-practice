import io

import pandas as pd

text = """item,amount,category
tea,20,food
bus,50,travel
pen,10,study
lunch,80,food
"""
df = pd.read_csv(io.StringIO(text))

assert list(df.columns) == ["item", "amount", "category"]
assert len(df) == 4
assert df["amount"].sum() == 160
assert df["amount"].max() == 80

big = df[df["amount"] > 15]
assert list(big["item"]) == ["tea", "bus", "lunch"]

by_category = df.groupby("category")["amount"].sum()
assert by_category["food"] == 100
assert by_category["travel"] == 50
print("all checks passed")
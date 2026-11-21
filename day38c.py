import pandas as pd

y = pd.Series([0, 0, 1, 1, 1])

print(y.value_counts())
print(y.mean())
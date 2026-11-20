import io

import pandas as pd

text = """name,marks,city
asha,80,surat
ravi,,surat
zoya,90,pune
zoya,90,pune
ben,40,
"""

df = pd.read_csv(io.StringIO(text))

assert len(df) == 5
assert df["marks"].isna().sum() == 1
assert df["city"].isna().sum() == 1

no_duplicates = df.drop_duplicates()
assert len(no_duplicates) == 4

filled = no_duplicates.fillna({"marks": 0, "city": "unknown"})
assert filled["marks"].isna().sum() == 0
assert list(filled["city"]) == ["surat", "surat", "pune", "unknown"]
assert filled["marks"].sum() == 210

dropped = no_duplicates.dropna()
assert list(dropped["name"]) == ["asha", "zoya"]

mean_marks = no_duplicates["marks"].mean()
assert mean_marks == 70
repaired = no_duplicates.fillna({"marks": mean_marks})
assert repaired["marks"].isna().sum() == 0
print("all checks passed")
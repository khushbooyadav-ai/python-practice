import io

import pandas as pd

text = """name,marks,subject
asha,80,maths
ravi,60,maths
zoya,90,science
ben,40,science
"""

df = pd.read_csv(io.StringIO(text))

assert list(df.columns) == ["name", "marks", "subject"]
assert len(df) == 4
assert df["marks"].mean() == 67.5
assert df["marks"].max() == 90

passed = df[df["marks"] >= 60]
assert list(passed["name"]) == ["asha", "ravi", "zoya"]

by_subject = df.groupby("subject")["marks"].mean()
assert by_subject["maths"] == 70
assert by_subject["science"] == 65

ranked = df.sort_values("marks", ascending=False)
assert list(ranked["name"]) == ["zoya", "asha", "ravi","ben"]
assert ranked.iloc[0]["name"] == "zoya"

print("all checks passed")
import io

import pandas as pd

text = """student,score,subject
asha,70,maths
ravi,,maths
zoya,90,
zoya,90,
ben,50,science
"""

df = pd.read_csv(io.StringIO(text))

assert len(df) == 5
assert df["score"].isna().sum() == 1
assert df["subject"].isna().sum() == 2

no_duplicates = df.drop_duplicates()
assert len(no_duplicates) == 4

filled = no_duplicates.fillna({"score": 0, "subject": "none"})
assert filled["score"].isna().sum() == 0
assert list(filled["subject"]) == ["maths", "maths", "none", "science"]
assert filled["score"].sum() == 210

dropped = no_duplicates.dropna()
assert list(dropped["student"]) == ["asha", "ben"]

mean_score = no_duplicates["score"].mean()
assert mean_score == 70
repaired = no_duplicates.fillna({"score": mean_score})
assert repaired["score"].isna().sum() == 0

missing_score = df[df["score"].isna()]
assert list(missing_score["student"]) == ["ravi"]

print("all checks passed")
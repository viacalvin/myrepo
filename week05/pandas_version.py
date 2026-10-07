import pandas as pd

df = pd.read_csv("scores.csv")
df["score"] = pd.to_numeric(df["score"], errors="coerce")
result = df.groupby("category")["score"].mean().round(2)
print(result)

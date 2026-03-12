import pandas as pd

data = {
    "name": ["kim","lee","park"],
    "age": [23,25,21],
    "score": [90,85,88]
}

df = pd.DataFrame(data)
print(df[["age", "score"]].values)
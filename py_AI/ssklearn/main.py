import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data = {
    "age": [20, 25, np.nan, 30],
    "score": [80, np.nan, 90, 95]
}

df = pd.DataFrame(data)

imputer = SimpleImputer(strategy="mean")
result = imputer.fit_transform(df)
result_df = pd.DataFrame(result, columns=df.columns)
print(result_df)

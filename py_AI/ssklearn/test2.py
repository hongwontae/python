import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder


df = pd.read_csv('Data.csv')
x = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

impute = SimpleImputer(missing_values=np.nan, strategy='mean')
impute.fit(x[:, 1:3])
x[:, 1:3] = impute.transform(x[:,1:3])

ct = ColumnTransformer(
    transformers=[("encoder", OneHotEncoder(), [0])],
    remainder="passthrough"
)

x = ct.fit_transform(x)

le = LabelEncoder()
y = le.fit_transform(y)

print(y)



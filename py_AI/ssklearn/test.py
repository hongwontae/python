import pandas as pd;
import numpy as np;
from sklearn.impute import SimpleImputer

df = pd.read_csv('test.csv')

# 행렬
x = df.iloc[:, :-1].values

# 백터
y = df.iloc[:, -1].values

print(x)
print(y)

impute = SimpleImputer(missing_values=np.nan, strategy='mean')
impute.fit(x)
x = impute.transform(x)

print(x)

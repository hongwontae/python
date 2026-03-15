import pandas as pd;
import numpy as np;
from sklearn.impute import SimpleImputer

df = pd.read_csv('Data.csv')
x = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
print(x)
print(y)

impute = SimpleImputer(missing_values=np.nan, strategy='mean')
impute.fit(x[:, 1:3])
x[:, 1:3] = impute.transform(x[:, 1:3])

print(x)



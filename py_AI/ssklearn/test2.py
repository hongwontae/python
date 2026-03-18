import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split


df = pd.read_csv('Data.csv')
## numpy arr
x = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

impute = SimpleImputer(missing_values=np.nan, strategy='mean')
# impute로 모든 행 + 열은 1에서 2
impute.fit(x[:, 1:3])
# impute.transformd은 arr 반환 -> fit으로 계산된거 처리
x[:, 1:3] = impute.transform(x[:,1:3])

# np arr 열 -> 행 처리
ct = ColumnTransformer(
    transformers=[("encoder", OneHotEncoder(), [0])],
    remainder="passthrough"
)
x = ct.fit_transform(x)

le = LabelEncoder()
y = le.fit_transform(y)

# Data Splitting Train and Test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1, stratify=y)


# 특성 스케일링
sc = StandardScaler()
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
x_test[:, 3:] = sc.transform(x_test[:, 3:])
print(x_train)
print(x_test)



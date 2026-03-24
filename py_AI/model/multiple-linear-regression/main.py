import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv('50_Startups.csv')
x = df.iloc[:,:-1].values
y = df.iloc[:, -1].values

# 3개의 카테고리를 one-hot-encoder으로 변환완료
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
x = np.array(ct.fit_transform(x))



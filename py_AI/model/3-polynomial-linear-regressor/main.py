import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


dataset = pd.read_csv('Position_Salaries.csv')

# 행렬을 가지고 오기 위한 문법
x = dataset.iloc[:, 1:-1].values
# 백터
y = dataset.iloc[:, -1].values

# 단순 선형 회귀 모델 구축
simple_regressor = LinearRegression()
simple_regressor.fit(x,y)

# 다항식 선형 회귀를 위한 전처리



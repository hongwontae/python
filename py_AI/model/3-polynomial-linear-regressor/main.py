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
lin_reg = LinearRegression()
lin_reg.fit(x,y)

# 다항식 선형 회귀를 위한 전처리
poly_reg = PolynomialFeatures(degree=2)
x_poly = poly_reg.fit_transform(x)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly, y)

# graph Simple Linear Regressor
plt.scatter(x,y, color='red')
plt.plot(x, lin_reg.predict(x), color='blue')
plt.title('Truth or Bluff (Linear Regressor)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# Graph Poly Linear Regressor
plt.scatter(x,y, color='red')
plt.plot(x, lin_reg2.predict(poly_reg.fit_transform(x)), color='blue')
plt.title('Truth or Bluff (Poly Regressor)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

print(lin_reg.predict([[6.5]]))
print(lin_reg2.predict(poly_reg.fit_transform([[6.5]])))
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

# Download and prepare the data
lifesat = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

#print(lifesat.head(27))

# Visualize the data
lifesat.plot(kind='scatter', grid=True,
x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show()

# Select a linear model
#model = LinearRegression()  # 선형 회귀 모델 적용
model = KNeighborsRegressor(n_neighbors=3)  # 한국과 1인당 gdp가 가장 가까운 세 나라

# Train the model
model.fit(X, y)

# Make a prediction for Cyprus
X_new = [[32_142.0]] # Cyprus' GDP per capita in 2020
print(model.predict(X_new)) # output: [[6.30165767]]

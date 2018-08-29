import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from machine_learning.utils.utils import scatter_data

#File
df = pd.read_csv("../data/house_prices.csv")

#Data splitting
X = df[["squareMeters"]].values #numpy-array format
Y = df[["salePrice"]].values

X_train, X_test, y_train, y_test = train_test_split(X,Y, random_state=0, test_size=0.25)
#print(X_train[:10])

#scatter_data(X_train, y_train, test_data=[X_test, y_test])

model = LinearRegression()
model.fit(X_train, y_train)

print("Intercept: " + str(model.intercept_))
print("Coef: " + str(model.coef_))

#give a prediction for test x
prediction = model.predict(X_test)

#visualize test data against test x and predicted y
#pred is the model
scatter_data(X_test, y_test, pred = [X_test, prediction])

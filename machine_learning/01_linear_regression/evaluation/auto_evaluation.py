import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("../../data/autos.csv")
print(df.head())

#Data
X1 = df[["kilometer"]]
X2 = df[["kilometer", "powerPS"]]
Y = df[["price"]]

model1 = LinearRegression()
model2 = LinearRegression()

#Model 1 --> Price prediction based on km
X1_train, X1_test, y_train, y_test = train_test_split(X1, Y, random_state=0, test_size=0.25)
model1.fit(X1_train, y_train)
print(model1.score(X1_test,y_test))

#Model 2 --> price prediction based on km and ps
X2_train, X2_test, y_train, y_test = train_test_split(X2, Y, random_state=0, test_size=0.25)
model2.fit(X2_train, y_train)
print(model2.score(X2_test,y_test))

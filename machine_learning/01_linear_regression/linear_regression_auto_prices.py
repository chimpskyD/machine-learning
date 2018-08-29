#Auto price prediction based on km

import pandas as pd
from sklearn.linear_model import LinearRegression

#File
df = pd.read_csv("../data/autos.csv")

#scatter_data(df["kilometer"], df["price"])

X = df[["kilometer"]]
Y = df[["price"]]

#Model
model = LinearRegression()
model.fit(X,Y)

print("Intercept: " + str(model.intercept_))
print("Coef: " + str(model.coef_))

values = [[0],[130000]]
prediction = model.predict(values)

#scatter_data(X,Y, pred=[values,prediction] )

print(model.predict([[50000]]))
"""Simple Linear Regression """

#imports
import pandas as pd
from sklearn.linear_model import LinearRegression
from machine_learning.utils.utils import scatter_data
# imports
import pandas as pd
from sklearn.linear_model import LinearRegression

from machine_learning.utils.utils import scatter_data

#Open file
df = pd.read_csv("./house_prices.csv")
print(df.head())


#Visualize data
#scatter_data(df["squareMeters"], df["salePrice"])


#Create a Linear Regression Model  - scikit-learn

X = df[["squareMeters"]]
Y = df[["salePrice"]]

model = LinearRegression()
#X,Y in bidimensional matrix
model.fit(X,Y)

#y = 3143.28481869 + 5071.35242619*x
print("Intercept: " + str(model.intercept_)) #3143.28481869
print("Coef: " + str(model.coef_)) #5071.35242619

values = [[40], [80], [30], [200]]
prediction = model.predict(values)

#visualize data
scatter_data(X,Y,pred=[values,prediction])



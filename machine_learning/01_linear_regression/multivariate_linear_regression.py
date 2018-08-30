#saleprice = w1*rooms+w2*profit + w0
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#read file
df = pd.read_csv("../data/hotels.csv", sep=";")
print(df.head())

print("Data: " + str(len(df)))
#Select feature
#Profit and square meters
X = df[["profit", "square_meters"]].values
#print(X[:10])

#Price
Y = df[["price mln"]].values
#print(Y[:10])


#Data splitting
X_train, X_test, y_train, y_test = train_test_split(X,Y, random_state=0, test_size=0.25)

model = LinearRegression()
#Training on train data (X and y)
model.fit(X_train, y_train)

#Intercept and coefficient of trained model
print(model.intercept_)
print(model.coef_)#2 values

#Intercept + [profit]*coef_1  + [squareMeters]*coef_2

#Prediction on Test data
y_predict = model.predict(X_test)

N = len(y_predict)
print("Prediction value - Real test value")
for i in range(N):
    print(str(y_predict[i][0]) + " - " + str(y_test[i][0]))
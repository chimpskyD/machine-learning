#saleprice = w1*rooms+w2*profit + w0
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#read file
df = pd.read_csv("../data/hotels.csv", sep=";")
print(df.head())

print("Data: " + str(len(df)))
scores = []
for i in range(len(df)):
    #Select feature
    #Profit and square meters
    #Only profit --> not really correlated
    #only square_meters --> really correlated
    X = df[["profit", "square_meters"]].values
    #Price
    Y = df[["price mln"]].values
    #Data splitting
    X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.25) #no random_state
    model = LinearRegression()
    #Training on train data (X and y)
    model.fit(X_train, y_train)
    #R square :)
    scores.append(model.score(X_test, y_test))

print(scores)

#Mean
print(np.mean(scores))

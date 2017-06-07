#!/bin/python
import sys
import pandas as pd
from sklearn import linear_model

# Read training data into a Pandas data-frame
data = pd.read_csv('trainingdata.txt', names=['charging_time', 'battery_life'])
df = pd.DataFrame(data)

# Remove 'noise' from the data
df_cleaned = df[df['battery_life'] < 8.00]

# Read charging time (independent variable) into a 1-D array
X = df_cleaned['charging_time']
# Reshape X into a vector, where every row represent a sample
X = X.values.reshape(len(X), 1)

# Read battery life (dependent variable) into a 1-D array
y = df_cleaned['battery_life']
# Reshape y into a vector, where every row represent a label
y = y.values.reshape(len(y), 1)

# Based on the available training data, if charging time is more than 4 hours,
# battery life is always 8 hours. So no need to run LinearRegression on any
# sample value less than 4. Simply return "8.00" as output. For the rest, run
# LinearRegression
timeCharged = float(raw_input().strip())
if val > 3.99:
    print "8.00"
else:
    reg = linear_model.LinearRegression()
    reg.fit(X, y)
    a = reg.predict(timeCharged)
    print ("%.2f" % a[0])

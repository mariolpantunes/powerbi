## Load dataset demand.csv

## Run the following code
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

dataset = dataset.dropna()

X = dataset[['Total Price', 'Base Price']]
y = dataset['Units Sold']


model = DecisionTreeRegressor()
model.fit(X, y)

preds = model.predict(X)

dataset['Predictions'] = preds
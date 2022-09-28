## Predict if a employer will leave company
## Load Dataset hr.csv

#Load in the dependencies
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler

#lets change categories to numbers
le = LabelEncoder()
dataset['Departments'] = le.fit_transform(dataset['Departments'])
dataset['salary'] = le.fit_transform(dataset['salary'])

#preprocess your data
y=dataset['left']
features = ['satisfaction_level', 'last_evaluation', 'number_project',
'average_montly_hours', 'time_spend_company', 'Work_accident',
'promotion_last_5years', 'Departments', 'salary']
X=dataset[features]

#lets scale the data
s = StandardScaler()
X = s.fit_transform(X)

#split and train the dataset
X_train,X_test,y_train,y_test = train_test_split(X,y)

#Let the model predict results
log = LogisticRegression()
log.fit(X_train,y_train)
y_pred = log.predict(X)
y_prob = log.predict_proba(X)

# Lets add the columns back to the dataframe
dataset['predictions'] = y_pred
dataset['probability of leaving'] = y_prob[:,1]



## K-Means Clustering in Power BI Using Python
## K-Means clustering is an unsupervised machine
## learning technique that allows you to find
## groups of data points that are similar to each other

# Load data with a script
import pandas as pd
from sklearn.datasets import load_iris

data = load_iris()
df = pd.DataFrame(data=data.data, columns=data.feature_names)

# Transform data to cluster them
import pandas as pd
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=4, init='k-means++', n_init=1, random_state=42)
kmeans_fit = kmeans.fit(dataset)

labels = kmeans_fit.labels_
dataset['Cluster'] = labels



## Prediction on time series
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

dataset.loc[:,'Yesterday'] = dataset['Births'].shift()
dataset.loc[:,'Diff'] = dataset.loc[:,'Yesterday'].diff()
dataset = dataset.dropna()

model = RandomForestRegressor(n_estimators = 42)

y = dataset['Births']
X = dataset[['Yesterday', 'Diff']]

model.fit(X, y)
dataset['Prediction'] = model.predict(X)
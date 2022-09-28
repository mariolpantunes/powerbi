## Handling Missing Data in Pandas
import pandas as pd
import numpy as np
df = pd.DataFrame.from_dict({
    'Name': ['Nik', 'Kate', 'Evan', 'Kyra', np.NaN],
    'Age': [33, 32, 40, 57, np.NaN],
    'Location': ['Toronto', 'London', 'New York', np.NaN, np.NaN]
})

# Dropping Values with Default Arguments
df = df.dropna()

# Dropping Records Only if All Records are Missing
df = df.dropna(how='all')

# Using .fillna() to Fill Missing Data
df = df.fillna(0)

# Filling Columns with Different Values
df = df.fillna({'Name': 'Someone', 'Age': 25, 'Location': 'USA'})

# Imputing a Missing Value
df['Age'] = df['Age'].fillna(df['Age'].mean())


## Working with Duplicate Data in Pandas
import pandas as pd
df = pd.DataFrame.from_dict({
    'Name': ['Nik', 'Kate', 'Evan', 'Kyra', 'Nik', 'Kate'],
    'Age': [33, 32, 40, 57, 33, 32],
    'Location': ['Toronto', 'London', 'New York', 'Atlanta', 'Toronto', 'Paris'],
    'Date Modified': ['2022-01-01', '2022-02-24', '2022-08-12', '2022-09-12', '2022-01-01', '2022-12-09']
})

# Dropping Duplicates with Default Arguments
df = df.drop_duplicates()

# Dropping Based on a Subset of Columns
df = df.sort_values(by='Date Modified', ascending=False)
df = df.drop_duplicates(subset=['Name', 'Age'], keep='first')

## Drop Outliers
import pandas as pd
df = pd.DataFrame.from_dict({
    'Name': ['Nik', 'Kate', 'Evan', 'Kyra', 'Nik', 'Kate'],
    'Age': [33, 32, 40, 57, 33, 150],
    'Location': ['Toronto', 'London', 'New York', 'Atlanta', 'Toronto', 'Paris'],
    'Date Modified': ['2022-01-01', '2022-02-24', '2022-08-12', '2022-09-12', '2022-01-01', '2022-12-09']
})

# Drop the 99% outlier
q = df['Age'].quantile(0.99)
df = df[df['Age'] < q]

# Drop low and high outliers
q_low = df['Age'].quantile(0.01)
q_hi  = df['Age'].quantile(0.99)

df_filtered = df[(df['Age'] < q_hi) & (df['Age'] > q_low)]
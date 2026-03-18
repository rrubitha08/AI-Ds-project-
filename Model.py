import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model():
    data = pd.read_csv('dataset.csv')
    X = data[['hours']]
    y = data['marks']

    model = LinearRegression()
    model.fit(X, y)

    return model

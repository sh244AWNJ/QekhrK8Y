# 代码生成时间: 2025-09-30 02:27:23
import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

"""
Time Series Predictor

This module provides a simple time series prediction functionality
using a linear regression model.
"""

class TimeSeriesPredictor:
    def __init__(self, api_url):
        """
        Initialize the TimeSeriesPredictor with an API URL.
        """
        self.api_url = api_url
        self.model = LinearRegression()

    def fetch_data(self):
        """
        Fetch time series data from the provided API URL.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()
            return pd.DataFrame(data)
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def prepare_data(self, df):
        """
        Prepare the data for training.
        """
        # Assuming the data frame has a 'date' column and a 'value' column
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)
        df = df['value'].values.reshape(-1, 1)
        return df

    def train_model(self, df):
        """
        Train the linear regression model on the prepared data.
        """
        X = df
        y = df
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        return self.model.score(X_test, y_test)

    def predict(self, X):
        """
        Make predictions using the trained model.
        """
        return self.model.predict(X)

    def evaluate(self, y_test, y_pred):
        """
        Evaluate the model using mean squared error.
        """
        mse = mean_squared_error(y_test, y_pred)
        print(f"Mean Squared Error: {mse:.2f}")

    def run(self):
        """
        Run the prediction pipeline.
        """
        df = self.fetch_data()
        if df is not None:
            df = self.prepare_data(df)
            score = self.train_model(df)
            print(f"Model R^2 score: {score:.2f}")
            y_pred = self.predict(df)
            self.evaluate(df, y_pred)

# Example usage
if __name__ == '__main__':
    api_url = 'https://api.example.com/time-series-data'
    predictor = TimeSeriesPredictor(api_url)
    predictor.run()
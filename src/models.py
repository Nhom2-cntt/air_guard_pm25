"""
models.py - Forecasting models for PM2.5
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from datetime import datetime, timedelta

class PM25Forecaster:
    def __init__(self):
        self.model = LinearRegression()
        self.is_trained = False
    
    def prepare_features(self, data, lookback=24):
        """Prepare features for forecasting"""
        features = []
        targets = []
        
        for i in range(lookback, len(data) - 1):
            # Use previous 'lookback' hours as features
            X = data['PM2.5'].values[i-lookback:i]
            # Next hour as target
            y = data['PM2.5'].values[i]
            
            features.append(X)
            targets.append(y)
        
        return np.array(features), np.array(targets)
    
    def train(self, data, lookback=24):
        """Train the model"""
        X, y = self.prepare_features(data, lookback)
        
        if len(X) == 0:
            print("Not enough data for training")
            return False
        
        self.model.fit(X, y)
        self.is_trained = True
        self.lookback = lookback
        
        # Calculate training error
        y_pred = self.model.predict(X)
        mse = mean_squared_error(y, y_pred)
        mae = mean_absolute_error(y, y_pred)
        
        print(f"Model trained successfully")
        print(f"Training MSE: {mse:.2f}")
        print(f"Training MAE: {mae:.2f}")
        
        return True
    
    def forecast(self, recent_data, hours=24):
        """Forecast next hours"""
        if not self.is_trained:
            print("Model not trained yet")
            return None
        
        forecasts = []
        current_data = recent_data.copy()
        
        for _ in range(hours):
            # Use last 'lookback' values
            X = current_data[-self.lookback:].reshape(1, -1)
            
            # Predict next value
            next_value = self.model.predict(X)[0]
            forecasts.append(next_value)
            
            # Update current data with prediction
            current_data = np.append(current_data, next_value)
        
        return forecasts

def main():
    """Test the forecaster"""
    print("Testing PM25Forecaster...")
    
    # Generate sample data
    dates = pd.date_range(end=datetime.now(), periods=168, freq='H')
    pm25 = 30 + 15 * np.sin(2 * np.pi * np.arange(168) / 24) + np.random.normal(0, 5, 168)
    pm25 = np.maximum(pm25, 10)
    
    data = pd.DataFrame({
        'timestamp': dates,
        'PM2.5': pm25
    })
    
    # Train model
    forecaster = PM25Forecaster()
    forecaster.train(data, lookback=24)
    
    # Make forecast
    recent_data = data['PM2.5'].values[-24:]
    forecasts = forecaster.forecast(recent_data, hours=12)
    
    if forecasts is not None:
        print(f"\nForecast for next 12 hours:")
        for i, value in enumerate(forecasts, 1):
            print(f"Hour {i:2d}: {value:.1f} μg/m3")
        
        avg_forecast = np.mean(forecasts)
        print(f"\nAverage forecast: {avg_forecast:.1f} μg/m3")
        
        if avg_forecast > 50:
            print("Warning: Forecast indicates poor air quality")

if __name__ == "__main__":
    main()

"""
air_quality.py - AIR GUARD core module
For PM2.5 forecasting and AQI calculation
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class AirQualityAnalyzer:
    def __init__(self, station_id="ST001"):
        self.station_id = station_id
        self.data = None
    
    def generate_hourly_data(self, days=7):
        """Generate hourly PM2.5 data"""
        hours = days * 24
        timestamps = pd.date_range(
            end=datetime.now(),
            periods=hours,
            freq='H'
        )
        
        # Create realistic PM2.5 data with daily pattern
        pm25_values = []
        for i in range(hours):
            hour_of_day = i % 24
            # Higher during day, lower at night
            daily_pattern = 20 * np.sin(2 * np.pi * (hour_of_day - 6) / 24)
            # Random noise
            noise = np.random.normal(0, 5)
            # Base level
            base = 30
            
            pm25 = base + daily_pattern + noise
            pm25 = max(10, pm25)  # Minimum 10
            pm25_values.append(round(pm25, 2))
        
        self.data = pd.DataFrame({
            'timestamp': timestamps,
            'station_id': self.station_id,
            'PM2.5': pm25_values
        })
        
        return self.data
    
    def calculate_aqi(self, pm25):
        """Calculate AQI from PM2.5"""
        if pm25 <= 12.0:
            return int((50/12.0) * pm25)
        elif pm25 <= 35.4:
            return int(51 + (49/23.4) * (pm25 - 12.1))
        elif pm25 <= 55.4:
            return int(101 + (49/20.0) * (pm25 - 35.5))
        elif pm25 <= 150.4:
            return int(151 + (49/94.9) * (pm25 - 55.5))
        else:
            return int(201 + (99/100.0) * (pm25 - 150.5))
    
    def analyze_station(self):
        """Analyze air quality for station"""
        if self.data is None:
            self.generate_hourly_data(3)
        
        stats = {
            'station': self.station_id,
            'records': len(self.data),
            'avg_pm25': float(self.data['PM2.5'].mean()),
            'max_pm25': float(self.data['PM2.5'].max()),
            'min_pm25': float(self.data['PM2.5'].min()),
            'hours_above_50': int((self.data['PM2.5'] > 50).sum())
        }
        
        return stats

def main():
    """Test the module"""
    analyzer = AirQualityAnalyzer("ST001")
    data = analyzer.generate_hourly_data(2)
    stats = analyzer.analyze_station()
    
    print("AIR GUARD Analysis Results:")
    print("=" * 40)
    for key, value in stats.items():
        print(f"{key}: {value}")
    
    # Calculate AQI for sample values
    print("\nAQI Examples:")
    samples = [25, 42, 65, 120]
    for pm25 in samples:
        aqi = analyzer.calculate_aqi(pm25)
        level = "Good" if aqi <= 50 else "Moderate" if aqi <= 100 else "Unhealthy"
        print(f"PM2.5: {pm25} -> AQI: {aqi} ({level})")

if __name__ == "__main__":
    main()

"""
data_loader.py - Load air quality data
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class DataLoader:
    def __init__(self):
        self.data = None
    
    def generate_sample_data(self, station_id="ST001", days=7):
        """Generate sample PM2.5 data"""
        hours = days * 24
        timestamps = pd.date_range(
            end=datetime.now(),
            periods=hours,
            freq='H'
        )
        
        # Create PM2.5 data
        pm25_values = []
        for i in range(hours):
            hour = i % 24
            # Higher during daytime (8 AM - 6 PM)
            if 8 <= hour <= 18:
                base = 40
            else:
                base = 25
            
            # Add some randomness
            variation = np.random.normal(0, 8)
            pm25 = max(10, base + variation)
            pm25_values.append(round(pm25, 2))
        
        self.data = pd.DataFrame({
            'timestamp': timestamps,
            'station_id': station_id,
            'PM2.5': pm25_values,
            'temperature': 25 + 5 * np.sin(2 * np.pi * np.arange(hours) / 24) + np.random.normal(0, 2, hours),
            'humidity': 65 + 10 * np.random.randn(hours)
        })
        
        return self.data
    
    def calculate_statistics(self):
        """Calculate basic statistics"""
        if self.data is None:
            return None
        
        stats = {
            'total_records': len(self.data),
            'avg_pm25': float(self.data['PM2.5'].mean()),
            'max_pm25': float(self.data['PM2.5'].max()),
            'min_pm25': float(self.data['PM2.5'].min()),
            'hours_above_50': int((self.data['PM2.5'] > 50).sum()),
            'date_range': {
                'start': self.data['timestamp'].min().strftime('%Y-%m-%d %H:%M'),
                'end': self.data['timestamp'].max().strftime('%Y-%m-%d %H:%M')
            }
        }
        
        return stats

def main():
    """Test the data loader"""
    print("Testing DataLoader...")
    
    loader = DataLoader()
    data = loader.generate_sample_data("ST001", 3)
    stats = loader.calculate_statistics()
    
    print(f"Generated {stats['total_records']} records")
    print(f"Time range: {stats['date_range']['start']} to {stats['date_range']['end']}")
    print(f"PM2.5 average: {stats['avg_pm25']:.1f} μg/m3")
    print(f"PM2.5 maximum: {stats['max_pm25']:.1f} μg/m3")
    print(f"Hours above safe limit: {stats['hours_above_50']}")
    
    # Save to CSV
    data.to_csv('data/sample_pm25_data.csv', index=False)
    print("Data saved to: data/sample_pm25_data.csv")

if __name__ == "__main__":
    main()

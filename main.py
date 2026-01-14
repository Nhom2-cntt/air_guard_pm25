import pandas as pd
import numpy as np

print("AIR GUARD - PM2.5 Forecasting System")
print("=" * 40)

# Create sample air quality data
data = {
    "Station": ["ST001", "ST002", "ST003", "ST004", "ST001"],
    "Date": pd.date_range("2024-01-01", periods=5),
    "PM2.5": [35.2, 42.8, 28.5, 55.3, 39.7],
    "Temperature": [25.3, 27.1, 23.8, 26.5, 24.9],
    "Humidity": [65, 72, 58, 68, 62]
}

df = pd.DataFrame(data)
print("Air Quality Data:")
print(df)
print()

# Calculate statistics
avg_pm25 = df["PM2.5"].mean()
max_pm25 = df["PM2.5"].max()
stations = df["Station"].unique()

print(f"Statistics:")
print(f"  Average PM2.5: {avg_pm25:.1f} μg/m3")
print(f"  Maximum PM2.5: {max_pm25:.1f} μg/m3")
print(f"  Number of stations: {len(stations)}")

# Check safety threshold
if max_pm25 > 50:
    print("\nALERT: PM2.5 exceeds safe limit (50 μg/m3)")
    print("   Recommendations:")
    print("   - Limit outdoor activities")
    print("   - Wear N95 mask")
    print("   - Use air purifier")
else:
    print("\nAir quality within safe limits")

print("=" * 40)
print("AIR GUARD system operational!")

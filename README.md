# AIR GUARD - PM2.5 Forecasting & AQI Alert System

## Overview
AIR GUARD is a system for predicting PM2.5 concentrations and generating Air Quality Index (AQI) alerts.

## Features
- PM2.5 concentration forecasting
- AQI calculation and classification
- Multi-station monitoring
- Health recommendations based on air quality

## Project Structure
air_guard_pm25/
├── data/                    # Air quality data
├── src/                     # Source code
│   └── air_quality.py      # Core air quality module
├── notebooks/              # Analysis notebooks
├── main.py                 # Main application
└── requirements.txt        # Dependencies

## Quick Start
# Install dependencies
pip install -r requirements.txt

# Run AIR GUARD system
python main.py

# Test core module
python src/air_quality.py

## Dependencies
- pandas>=2.0.0
- numpy>=1.24.0
- scikit-learn>=1.3.0

## Example Output
AIR GUARD - PM2.5 Forecasting System
Air Quality Data:
Station       Date  PM2.5  Temperature  Humidity
ST001   2024-01-01   35.2         25.3        65
ALERT: PM2.5 exceeds safe limit (50 μg/m3)

## Team
Air Quality Monitoring Team

## License
MIT License

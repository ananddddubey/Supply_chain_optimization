import pandas as pd
import numpy as np
from datetime import timedelta

# Generate serial numbers
serial_numbers = list(range(1, 10001))

# Generate random dates
start_date = pd.to_datetime('2022-01-01')
end_date = pd.to_datetime('2024-01-01')
date_range = pd.date_range(start=start_date, end=end_date, periods=10000)
dates = np.random.choice(date_range, size=10000, replace=True)

# Generate random product IDs
product_ids = np.random.randint(1, 100, size=10000)

# Generate random demand and inventory levels
demand = np.random.randint(1, 1000, size=10000)
inventory = np.random.randint(1, 1000, size=10000)

# Create a DataFrame
data = pd.DataFrame({
    'Serial No.': serial_numbers,
    'Date': dates,
    'Product ID': product_ids,
    'Demand': demand,
    'Inventory': inventory
})

# Save the DataFrame to a CSV file
data.to_csv('synthetic_data.csv', index=False)

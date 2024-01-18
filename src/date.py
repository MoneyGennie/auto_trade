import pandas as pd
from datetime import datetime, timedelta

# Sample DataFrame
df = pd.DataFrame({
    'date': ['2024-01-11 13:45:00', '2024-01-11 14:00:00', '2024-01-11 15:30:00'],
    'open': [100, 110, 120],
    'high': [120, 115, 130],
    'low': [90, 105, 110],
    'close': [110, 100, 125],
})

# Get today's date and format it as a string
today_date_str = datetime.now().date()

# Create the target string with today's date
target_date_str = f"{today_date_str} 15:30:00"
print(target_date_str)

# Convert the 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Identify the index of the last row with 'date' equal to the target date
last_row_index = df[df['date'] == target_date_str].index

# Drop the last row by index
df.drop(last_row_index, inplace=True)

# Display the modified DataFrame
print(df)

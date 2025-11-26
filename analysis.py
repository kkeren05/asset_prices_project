import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("historical_data.csv")

# Clean dataset
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')
df = df.dropna(subset=['Close/Last'])

# Plot closing price
plt.plot(df['Date'], df['Close/Last'])
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title("Closing Price Over 1 Year")
plt.show()

# Daily percentage change
df['Pct_Change'] = df['Close/Last'].pct_change() * 100

# Plot percentage change
plt.plot(df['Date'], df['Pct_Change'])
plt.xlabel("Date")
plt.ylabel("Daily % Change")
plt.title("Daily Percentage Price Change")
plt.show()

# Standard deviation
std_dev = df['Pct_Change'].std()
print("Standard deviation of daily % change:", std_dev)
import pandas as pd
import matplotlib.pyplot as plt

file_path = "solar_irradiance_data.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")
print("Columns in DataFrame:", df.columns.tolist())  
print(df.head())  
df.columns = df.columns.str.strip()  
df.columns = df.columns.str.lower()  
print(df.columns.tolist())  




df['Date'] = pd.to_datetime(df['date'])

df = df.sort_values(by='Date')
plt.figure(figsize=(10, 5))

plt.plot(df['Date'], df['irradiance'], marker='o', linestyle='-', color='b', label='Irradiance')
plt.xlabel("Date")
plt.ylabel("Irradiance (W/m²)")  
plt.title("Solar Irradiance Trend Over Time")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
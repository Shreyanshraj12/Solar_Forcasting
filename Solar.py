import requests
import pandas as pd


url = ("https://power.larc.nasa.gov/api/temporal/daily/point?"
       "parameters=ALLSKY_SFC_SW_DWN&"
       "community=SB&"
       "longitude=78.65&"
       "latitude=9.15&"
       "start=20220101&"
       "end=20250224&"
       "format=JSON")


response = requests.get(url)
data = response.json()


irradiance_data = data['properties']['parameter']['ALLSKY_SFC_SW_DWN']


df = pd.DataFrame(irradiance_data.items(), columns=['Date', 'Solar Irradiance (W/m²)'])
df['Date'] = pd.to_datetime(df['Date'])  


df.to_excel("solar_irradiance_data.xlsx", index=False)

print("Excel file 'solar_irradiance_data.xlsx' saved successfully!")

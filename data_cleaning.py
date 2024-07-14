import pandas as pd
import os

dir = os.getcwd()
df = pd.read_excel('Final_data_cleaned.xlsx')

df = df.drop(columns=df.columns[0])

df[df.columns[:-1]] = df[df.columns[:-1]].astype('string')
to_rename = ['WEATHER_ARRIVAL(celsius)', 'WIND_ARRIVAL(kts)', 'DIRECTION_ARRIVAL(degrees)',
       'WEATHER_DEPARTURE(celcius)', 'WIND_DEPARTURE(kts)', 'DIRECTION_DEPARTURE(degrees)']
to_be_renamed = list(df.columns[10:16])

dict1 = dict()
for x,y in zip(to_be_renamed, to_rename):
    dict1[x] = y 
df  = df.rename(columns=dict1)

for col in to_rename:
    df[col] = df[col].apply(lambda x:x.split(" ")[0])

df.AIRLINE = df.AIRLINE.astype('string').apply(lambda x:x.split("(")[0].strip())

#data columns
date_cols= ['DATE','Scheduled_departures', 'Actual_departures', 'Flight_duration', 'Scheduled_arrival']
####

df.to_excel('cleaned.xlsx')

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors, patches
import seaborn as sns
from datetime import datetime
import numpy as np

# read in data from SWPC and fix the first row
df=pd.read_json('https://services.swpc.noaa.gov/products/solar-wind/plasma-2-hour.json')
df.columns=['Date', 'Density', 'Speed', 'temperature']
df = df.drop(index=0)

#move to lists
date = df['Date'].to_list()
speed = df['Speed'].to_list()
density = df['Density'].to_list()

# import plotly
import plotly.graph_objects as go
import plotly.express as px


# remake dataframe specifically for solar wind speed
df= pd.DataFrame({'datetime':date, 'speed':speed})

#convert speed to float values
for i in range(0, len(df['speed'])):
    df['speed'][i]=float(df['speed'][i])

# plot using plotly express
fig = px.line(df, x='datetime', y='speed', title="Testing")

# write out plot to html in order to embed into dashboard websites
fig.write_html('TEST.html')
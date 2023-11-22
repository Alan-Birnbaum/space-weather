import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np

df=pd.read_json('https://services.swpc.noaa.gov/products/solar-wind/plasma-2-hour.json')
df.columns=['Date', 'Density', 'Speed', 'temperature']
df = df.drop(index=0)

date = df['Date'].to_list()
speed = df['Speed'].to_list()

maxNum=0
for i in range(0, len(date)):
    date[i] = date[i][:-7]
    date[i] = datetime.strptime(date[i], '%Y-%m-%d %H:%M')
    speed[i] = float(speed[i])
    if speed[i]> maxNum:
        maxNum=speed[i]
        
if maxNum < 400.0:
    plt.figure(figsize=(20, 14), facecolor='#999999')
    sns.set_theme()
    plt.fill_between(date, 200, speed, color='green', alpha=0.8)
    plt.ylim([np.min(speed) - 20, np.max(speed) + 40])
    plt.xlim([date[0], date[-1]])
    plt.ylabel('Solar Wind Speed(km/s)', fontsize=20)
    plt.xlabel('Date', fontsize=20)
    plt.title('2hr Solar Wind Speed(km/s)', fontsize=24)
    plt.savefig('Solar_Wind.png',bbox_inches='tight')
    
elif maxNum >= 400.0 and maxNum < 500.0:
    plt.figure(figsize=(20, 14),facecolor='#999999')
    sns.set_theme()
    plt.fill_between(date, 200, speed, color='yellow', alpha=0.8)
    plt.ylim([np.min(speed) - 20, np.max(speed) + 40])
    plt.xlim([date[0], date[-1]])
    plt.ylabel('Solar Wind Speed(km/s)', fontsize=20)
    plt.xlabel('Date', fontsize=20)
    plt.title('2hr Solar Wind Speed(km/s)', fontsize=24)
    plt.savefig('Solar_Wind.png',bbox_inches='tight')
    
elif maxNum >= 500.0 and maxNum < 600.0:
    plt.figure(figsize=(20, 14),facecolor='#999999')
    sns.set_theme()
    plt.fill_between(date, 200, speed, color='orange', alpha=0.8)
    plt.ylim([np.min(speed) - 20, np.max(speed) + 40])
    plt.xlim([date[0], date[-1]])
    plt.ylabel('Solar Wind Speed(km/s)', fontsize=20)
    plt.xlabel('Date', fontsize=20)
    plt.title('2hr Solar Wind Speed(km/s)', fontsize=24)
    plt.savefig('Solar_Wind.png',bbox_inches='tight')
    
else:
    plt.figure(figsize=(20, 14),facecolor='#999999')
    sns.set_theme()
    plt.fill_between(date, 200, speed, color='red', alpha=0.8)
    plt.ylim([np.min(speed) - 20, np.max(speed) + 40])
    plt.xlim([date[0], date[-1]])
    plt.ylabel('Solar Wind Speed(km/s)', fontsize=20)
    plt.xlabel('Date', fontsize=20)
    plt.title('2hr Solar Wind Speed(km/s)', fontsize=24)
    plt.savefig('Solar_Wind.png',bbox_inches='tight')
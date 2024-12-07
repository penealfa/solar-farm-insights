# scripts/time_series_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def plot_time(data, time_column, metrics):
    data[time_column]= pd.to_datetime(data[time_column])
    data['Month'] = data[time_column].dt.to_period('M')
    monthly_avg = data.groupby('Month')[metrics].mean()
    print(monthly_avg)
    monthly_avg.reset_index(inplace=True)

    for metric in metrics:
         if metric in data.columns:
             plt.figure(figsize=(12, 6))
             plt.plot(monthly_avg['Month'].astype(str), monthly_avg[metric], marker='o', label=metric)
             plt.plot(monthly_avg['Month'].astype(str), monthly_avg[metric], marker='o', label=metric)
             plt.title(f"{metric} Over Time ({time_column})")
             plt.xlabel("Time")
             plt.ylabel(metric)
             plt.grid(True)
             plt.show()
         else:
             print(f"Metric '{metric}' not found in the data.")

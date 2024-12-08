import pandas as pd
import matplotlib.pyplot as plt

def plot_time(data, time_column, metrics):
    data[time_column] = pd.to_datetime(data[time_column])
    data['Month'] = data[time_column].dt.to_period('M')
    monthly_avg = data.groupby('Month')[metrics].mean()
    print(monthly_avg)
    monthly_avg.reset_index(inplace=True)
    plt.figure(figsize=(15, 10))
    for metric in metrics:
        if metric in data.columns:
            plt.plot(monthly_avg['Month'].astype(str), 
                     monthly_avg[metric], 
                     marker='o', 
                     label=metric)
        else:
            print(f"Metric '{metric}' not found in the data.")
    plt.title(f"Metrics Over Time ({time_column})")
    plt.legend(title="Metrics") 
    plt.xlabel("Time")
    plt.ylabel("Values")
    plt.legend(title="Metrics")
    plt.tight_layout()
    plt.grid(True)
    plt.show()

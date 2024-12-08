import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def bubble_chart_analysis(data):
    x_var = "GHI"
    y_var = "Tamb"
    bubble_size = "RH"
    bubble_color = "WS"
    bubble_sizes = (data[bubble_size] - data[bubble_size].min()) / (data[bubble_size].max() - data[bubble_size].min()) * 500 + 20
    bin_edges = [0, 2, 5, 10, 15, 20, np.inf]
    bin_labels = ['Calm', 'Light Breeze', 'Moderate Breeze', 'Strong Breeze', 'Gale', 'Storm']
    data['WS_Class'] = pd.cut(data['WS'], bins=bin_edges, labels=bin_labels, include_lowest=True)
    grouped = data.groupby('WS_Class').agg({
            'GHI': 'mean',       # Average GHI
            'Tamb': 'mean',      # Average Temperature
            'RH': 'mean',        # Average Relative Humidity
        }).reset_index()
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(
        x=grouped[x_var],
        y=grouped[y_var],
        s=grouped['RH'] * 10,  # Scale bubble size for visibility
        c=range(len(grouped)),
        cmap="viridis",
        alpha=0.7,
        edgecolor="k",
    )
    cbar = plt.colorbar(scatter)
    cbar.set_label(f"{bubble_color} (m/s)", fontsize=12)
    plt.title(f"Bubble Chart: {x_var} vs {y_var} with Bubble Size as {bubble_size} and Color as {bubble_color}", fontsize=16)
    plt.xlabel(x_var, fontsize=12)
    plt.ylabel(y_var, fontsize=12)
    plt.tight_layout()
    plt.show()

 

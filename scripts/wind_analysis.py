import numpy as np
import pandas as pd
from windrose import WindroseAxes
import matplotlib.pyplot as plt


def wind_direction_and_speed_analysis(data):
    fig = plt.figure(figsize=(8, 8))
    ax = WindroseAxes.from_ax(fig=fig)
    ax.bar(data["WD"], data["WS"], normed=True, bins=np.arange(0, 20, 5), cmap=plt.cm.viridis, edgecolor='k')
    ax.set_title("Wind Rose - Distribution of Wind Speed and Direction")
    ax.legend(title="Wind Speed (m/s)", loc="best", fontsize=8)
    plt.show()

 

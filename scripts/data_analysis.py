import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import kurtosis, skew

def analyze_distribution(df, numerical_cols):
    recommendations = {}
    for col in numerical_cols:
        col_skew = skew(df[col], axis=0, bias=True)
        col_kurt = kurtosis(df[col], axis=0, fisher=True, bias=True)
        plt.figure(figsize=(10, 4))
        df[col].hist(bins=50, edgecolor='black')  # Adjust bins as needed for clarity
        plt.title(f"Histogram for {col}\nSkewness: {col_skew:.2f}, Kurtosis: {col_kurt:.2f}")
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.show()
    if abs(col_skew) < 0.5 and 2 < col_kurt < 4:  # Near-normal conditions
        recommendations[col] = "z-score"
    else:
        recommendations[col] = "iqr"
    return recommendations
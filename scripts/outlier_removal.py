import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import zscore

def remove_outliers_zscore(df, numerical_cols, threshold=3.0, visualize=False):

    df_filtered = df.copy()

    for col in numerical_cols:
        z_scores = np.abs(zscore(df_filtered[col]))
        outliers_mask = z_scores > threshold
        
        if visualize:
            plt.figure(figsize=(10, 6))
            plt.scatter(df_filtered.index, df_filtered[col], c='b', label='Original Data')
            plt.scatter(df_filtered.index[outliers_mask], df_filtered[col][outliers_mask], c='r', label='Outliers')
            plt.legend()
            plt.title(f"Original vs. Outliers - {col}")
            plt.show()
        
        df_filtered = df_filtered[~outliers_mask].reset_index(drop=True)
        
        print(f"Column: {col}")
        print(f"Original Rows: {len(df)}")
        print(f"Rows After Filtering: {len(df_filtered)}")
        print(f"Removed Outliers: {len(df) - len(df_filtered)}\n")
    
    return df_filtered

def plot_outliers_by_zscore(df, numerical_cols, threshold=3.0):

    df_filtered = df.copy()

    for col in numerical_cols:
        z_scores = np.abs(zscore(df_filtered[col]))
        outliers_mask = z_scores > threshold
        plt.figure(figsize=(10, 6))
        plt.scatter(df_filtered.index, df_filtered[col], c='b', label='Original Data')
        plt.scatter(df_filtered.index[outliers_mask], df_filtered[col][outliers_mask], c='r', label='Outliers')
        plt.legend()
        plt.title(f"Original vs. Outliers - {col}")
        plt.show()


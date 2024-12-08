import pandas as pd
import numpy as np

def clean_dataframe(data: pd.DataFrame) -> pd.DataFrame:
    # Cleans a DataFrame by removing rows containing NaN or infinite values. this is for the skewness and Kurtosis
    cleaned_data = data.replace([np.inf, -np.inf], np.nan)
    cleaned_data = cleaned_data.dropna()
    return cleaned_data

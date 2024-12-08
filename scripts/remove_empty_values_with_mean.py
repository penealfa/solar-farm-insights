import pandas as pd

def replace_empty_with_mean(data):
    data_copy = data.copy()
    for column in data.columns:
        if column != "Cleaning" and pd.api.types.is_numeric_dtype(data[column]):
            mean_value = data[column][data[column] != 0].mean()
            data_copy[column] = data[column].replace(0, mean_value)
    
    return data_copy

import pandas as pd
from scripts.load_data import load_csv_file
from scripts.utils import get_output_file_path

def merge_data(files, country_map, output_filename):
    merged_df = pd.DataFrame()
    for file, country in country_map.items():
        df = load_csv_file(file)
        df['Country'] = country
        merged_df = pd.concat([merged_df, df], ignore_index=True)
    output_file_path = get_output_file_path(output_filename)
    merged_df.to_csv(output_file_path, index=False)
    return merged_df 
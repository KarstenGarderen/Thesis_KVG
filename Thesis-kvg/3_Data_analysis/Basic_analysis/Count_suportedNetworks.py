import pandas as pd

file_path = '/Users/karsten/Downloads/Thesis/Results/Final_dataset.xlsx'  
df = pd.read_excel(file_path)

network_column = 'networks'

def count_unique_options(networks):
    unique_options = set([option.strip() for option in str(networks).split(',') if option.strip()])
    return len(unique_options)

df['UniqueOptionCount'] = df[network_column].apply(count_unique_options)

print(df)

output_file_path = '/Users/karsten/Downloads/Thesis/Results/networks_unique_options_count2.xlsx'
df.to_excel(output_file_path, index=False)


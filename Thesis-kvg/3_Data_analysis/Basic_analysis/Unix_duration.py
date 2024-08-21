import pandas as pd

file_path_new = '/Users/karsten/Downloads/Thesis/Results/Definief!.xlsx'
df_new = pd.read_excel(file_path_new)

df_new['start'] = pd.to_datetime(df_new['start'], unit='s')
df_new['end'] = pd.to_datetime(df_new['end'], unit='s')

df_new['Duration'] = df_new['end'] - df_new['start']

df_new['Duration_seconds'] = df_new['Duration'].dt.total_seconds()

output_path = '/Users/karsten/Downloads/Thesis/Results/unixresults.xlsx'
df_new.to_excel(output_path, index=False)


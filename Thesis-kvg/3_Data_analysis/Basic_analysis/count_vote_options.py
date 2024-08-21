import pandas as pd
import re

file_path = '/Users/karsten/Downloads/Thesis/Results/Final_dataset.xlsx' 
df = pd.read_excel(file_path)

proposal_column = 'choices'

def count_options(proposal):
    options = re.findall(r"'(.*?)'", proposal)
    return len(options)

df['OptionCount'] = df[proposal_column].apply(count_options)

print(df)

output_file_path = '/Users/karsten/Downloads/Thesis/Results/choises_dataset.xlsx'
df.to_excel(output_file_path, index=False)


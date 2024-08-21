import pandas as pd
import re

def count_external_links(text):
    if pd.isna(text):
        return 0
    urls = re.findall(r'(https?://\S+)', text)
    return len(urls)

file_path = '/Users/karsten/Downloads/Thesis/Results/Final_dataset.xlsx'  
df = pd.read_excel(file_path)


specific_column = 'body' 

df['link_count'] = df[specific_column].apply(count_external_links)


output_file_path = '/Users/karsten/Downloads/Thesis/Results/urlcount_dataset.xlsx'
df.to_excel(output_file_path, index=False)


import pandas as pd

def count_words(text):
    if pd.isna(text):
        return 0
    words = text.split()
    return len(words)

file_path = '/Users/karsten/Downloads/Thesis/Results/Final_dataset.xlsx' 
df = pd.read_excel(file_path)

df['word_count'] = df['body'].apply(count_words)

output_file_path = '/Users/karsten/Downloads/Thesis/Results/wordcount_dataset.xlsx'  
df.to_excel(output_file_path, index=False)


import pandas as pd

file_path = '/Users/karsten/Downloads/Copy_Final_Version.xlsx'
df = pd.read_excel(file_path)

def is_test_proposal(title):
    test_keywords = ['test', 'sample', 'example']
    title_lower = title.lower()
    for keyword in test_keywords:
        if keyword in title_lower:
            return True
    return False

df['is_test'] = df['title'].apply(is_test_proposal)

highlighted_file_path = '/Users/karsten/Downloads/Copy_Final_Version2.xlsx'
with pd.ExcelWriter(highlighted_file_path, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Proposals')
    workbook = writer.book
    worksheet = writer.sheets['Proposals']
    
    format_red = workbook.add_format({'bg_color': 'red', 'font_color': 'white'})
    for row_num, is_test in enumerate(df['is_test'], start=2):  
        if is_test:
            worksheet.write(row_num, df.columns.get_loc('title'), df.at[row_num-2, 'title'], format_red)

print(f"Initial dataset size: {len(df)}")
print(f"Number of test proposals: {df['is_test'].sum()}")
print(f"Highlighted dataset saved to: {highlighted_file_path}")

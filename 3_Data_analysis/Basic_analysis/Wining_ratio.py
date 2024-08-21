import pandas as pd

def calculate_winning_ratio(row):
    total = row.sum()
    if total == 0:
        return float('nan')
    winning_ratio = row.max() / total
    return winning_ratio


input_file = '/Users/karsten/Downloads/Thesis/Results/Final_dataset.xlsx'  
output_file = '/Users/karsten/Downloads/Thesis/Results/winning_ratios.xlsx'  

column_name = 'scores'  


df = pd.read_excel(input_file)

scores_df = df[column_name].apply(lambda x: pd.Series(eval(x)))

winning_ratios = scores_df.apply(calculate_winning_ratio, axis=1)

winning_ratios_df = pd.DataFrame(winning_ratios, columns=['winning_ratio'])
winning_ratios_df.to_excel(output_file, index=False)

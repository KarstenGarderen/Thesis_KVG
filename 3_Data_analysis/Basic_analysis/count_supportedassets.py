import pandas as pd


file_path = '/Users/karsten/Downloads/Thesis/Results/Playground.xlsx' 
df = pd.read_excel(file_path)


assets_column = 'symbols'


def count_unique_assets(assets):
    unique_assets = set([asset.strip() for asset in str(assets).split(',') if asset.strip()])
    return len(unique_assets)

df['UniqueAssetCount'] = df[assets_column].apply(count_unique_assets)

print(df)

output_file_path = '/Users/karsten/Downloads/Thesis/Results/supported_assets_unique_count.xlsx'
df.to_excel(output_file_path, index=False)


import pandas as pd

file_path = '/Users/karsten/Downloads/Thesis/Results/Final_dataset.xlsx'
xls = pd.ExcelFile(file_path)

df = pd.read_excel(file_path, sheet_name='Proposals')

def extract_from_json(json_str):
    try:
        data = eval(json_str)
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return '', '', ''
    
    networks = []
    strategies = []
    symbols = []
    
    def process_entry(entry, symbol):
        network = entry.get('network', '')
        if 'strategies' in entry['params']:
            for strategy in entry['params']['strategies']:
                networks.append(str(strategy.get('network', network)))
                strategies.append(str(strategy.get('name', '')))
                symbols.append(symbol)
        else:
            networks.append(str(network))
            symbols.append(symbol)
    
    for entry in data:
        symbol = entry['params'].get('symbol', '')
        process_entry(entry, symbol)
        if 'strategy' in entry['params']:
            sub_strategy = entry['params']['strategy']
            if isinstance(sub_strategy, dict):
                sub_symbol = sub_strategy['params'].get('symbol', symbol)
                process_entry(sub_strategy, sub_symbol)
            else:
                print(f"Unexpected sub_strategy type: {type(sub_strategy)} - {sub_strategy}")
    
    return ','.join(networks), ','.join(strategies), ','.join(symbols)

df[['networks', 'strategies', 'symbols']] = df['strategies'].apply(lambda x: pd.Series(extract_from_json(x)))

print(df[['networks', 'strategies', 'symbols']])

output_file_path = '/Users/karsten/Downloads/Thesis/Results/Copy_Final_Version3.xlsx'
with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Proposals', index=False)
    df[['networks', 'strategies', 'symbols']].to_excel(writer, sheet_name='Extracted Data', index=False)

print(f"Data saved to {output_file_path}")

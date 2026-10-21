import pandas as pd

def load_and_clean_data():
    data = pd.read_csv('matches.csv')

    data.rename(columns={'FTHG': 'Home_Goals', 'FTAG': 'Away_Goals', 'FTR': 'Result'}, inplace=True)
    print(data.isnull().sum())

    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y', errors='coerce', dayfirst=True, utc=True)

    data.to_csv('matches_cleaned.csv', index=False)
    
    return data


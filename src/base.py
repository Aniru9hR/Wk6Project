import pandas as pd


class Base:
    def __init__(self): 
        self.football_df = pd.read_csv(r'C:\Users\aniru\OneDrive\Documents\codingtemple\week6\Wk6Project\2022-2023 Football Player Stats.csv',encoding = "ISO-8859-1",sep=';')
        self.get_data()
    
    def get_data(self):
        self.football_df.columns = self.football_df.columns.str.lower()
        self.football_df.dropna(axis=0,inplace=True)
        self.football_df.drop_duplicates(subset=['player'],inplace=True)
        self.football_df['player'] = self.football_df['player'].str.replace('?',' ')
        print(self.football_df)
        return self.football_df

if __name__ == '__main__':
    c = Base()
    # c.get_data()
    c.football_df.to_csv('src/data/player_stats.csv', index=False)
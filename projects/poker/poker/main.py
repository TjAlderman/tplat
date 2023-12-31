import pandas as pd

class player:
    def __init__(self,name="Player",expenses=0,winnings=0):
        self.name = name
        self.expenses = expenses
        self.winnings = winnings


def distribute_winnings(players:list)->None:
    df = pd.DataFrame(columns=['Name','Balance'])
    for p in players:
        balance = p.winnings-p.expenses
        player_df = pd.DataFrame({'Name':[p.name],'Balance':[balance]})
        df = pd.concat([df,player_df],ignore_index=True)
    df = df.sort_values(by='Balance',ascending=False)
    print(df)
import pandas as pd
from scipy.optimize import linprog

class Player:
    def __init__(self,name="Player",expenses=0,winnings=0):
        self.name = name
        self.expenses = expenses
        self.winnings = winnings
        

def distribute_winnings(players: list)->None:
    df = pd.DataFrame(columns=['Name','Balance'])
    for p in players:
        balance = p.winnings-p.expenses
        player_df = pd.DataFrame({'Name':[p.name],'Balance':[balance]})
        df = pd.concat([df,player_df],ignore_index=True)
    df = df.sort_values(by='Balance',ascending=False)

    # determine if any miscounts occur. If an unacceptably large quantity is miscounted, return error.
    total = df['Balance'].sum()
    if abs(total)>5:
        raise Exception(f"Error! ${total} was {'lost' if total>0 else 'gained'} from the miscounts.")
    elif total==0:
        pass
    else:
        print(f"${total} was {'lost' if total>0 else 'gained'} from the miscounts. Proceeding...")

    # use linear programming to solve? 
    # psuedo code
    cost_function = x + y + z # cost function = number of transactions made by each person


    # use minimum spannig trees to solve ?



    print(df)
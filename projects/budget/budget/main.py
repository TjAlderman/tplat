import pandas as pd
import re
from typing import Union
from pathlib import Path
from datetime import datetime

# keys dict provide a level of abstraction that will ensure the program can easily be made compatible with other banks csv formats.
keys = {"Description" : ["Long description"], "Balance" : ["Debit amount"], "Date": ["Create date"]} # if using a new bank bank with differnt csv format, add as value 
matches =  {"TFR": ["tfr from t j alder"], "Takeout": ["subway", "mcdonalds", "bakery", "sushi", "anitagelato", "zambrero", "kfc", "ice cream", "monster cupbop", "the food co-op shop", "gangnam lane", "hello harry", "tilleys", "oporto", "ballistic burrito", "kebab", "dumpling", "spilt milk", "grease monkey", "colosseum italian", "melted toasties", "hungry jacks", "sharetea"], "Groceries": ["woolworths", "coles", "unique meats", "iga", "ziggys", "oz fish", "aldi", "butcher", "supabarn"], "Icecream":["spiltmilk"], "Petrol":["ampol", "bp", "7-eleven", "petroleum"], 
           "Physio":["woden integrated", "philip snare and feng"], "Doctor":["damian smith"], "Alcohol":["bws","liqourland", "hopscotch", "dollys", "one22", "austrian australian cl", "loquita", "king o malley s", "mooseheads", "civic pub", "fun time pony", "squeaky clean bar", "hotel kingston", "fiction club", "canberra north bowling", "transit bar", "thirsty camel", "bar beirut", "casino canberra", "tathra beach bowling", "tathra hotel", "the duxton"], "Dentist":[], 
           "Exercise":["club lime","dark carnival"], "Declined EFT":["declined eft fee"], "Car":["super cheap","bapcor", "bingle", "techworkz", "colmatt services"], 
           "Bunnings":["bunnings"], "Uber":["uber"], "Subscriptions":["remarkable", "chatgpt", "aldimobile"], "Parking":["parking"], "Games":["playstation"]}
categories = list(matches.keys())


class Transaction:
    """
    This class provides a level of abstraction that will ensure the program can easily be 
    made compatible with other banks csv formats.
    """
    def __init__(self, df: pd.DataFrame):
        self.columns = {"Description": None, "Balance": None, "Date": None}
        for d in keys["Description"]:
            if d in list(df.columns): self.columns["Description"] = d
        for b in keys["Balance"]:
            if b in list(df.columns): self.columns["Balance"] = b
        for t in keys["Date"]:
            if t in list(df.columns): self.columns["Date"] = t


    def store(self, row):
        self.description = row[self.columns["Description"]]
        self.balance = row[self.columns["Balance"]]
        self.date = row[self.columns["Date"]]
       


def categorise(description: str)->str:
    """
    This function sorts a Transaction.data["description"] attribute into a category.

    :param data: Transaction.data["description"] attribute.
    :type data: str
    :return: Identified category
    :rtype: str
    """
    
    # should figure out how to convert decsription to all lowercase so don't have to handle different capitalisation cases
    for cat in categories:
        for m in matches[cat]:
            if m in description.lower():
                return cat
    else:
        return "Unknown"
    
    
def main(fp, out: bool=False)-> None:
    """
    _summary_

    :param fp: filepath to .csv file containing bank statement of transactions.
    :type ƒp: str
    """
    # read in the data
    df = pd.read_csv(fp) 

    # first, find out what the description and balance headings are
    t = Transaction(df=df)
    # if description or balance were not found
    if None in list(t.columns.values()):
        raise Exception("Error! Unrecognised .csv structure...")
        
    
    # create a dataframe to hold all the sorted data (each category is a sheet)
    xlsx = {cat:{"Balance": [], "Description": [], "Date": []} for cat in categories} 
    xlsx["Unknown"] = {"Balance": [], "Description": [], "Date": []}
    xlsx["Total"] = {"Balance": []}

    for index, row in df.iterrows():
        t.store(row)
        cat = categorise(t.description)
        # ignore transfers between your own personal accounts
        if cat=="TFR":
            pass
        else:
            xlsx[cat]["Balance"].append(t.balance)
            xlsx[cat]["Description"].append(t.description)
            xlsx[cat]["Date"].append(t.date)
        
    # # Add totals field
    categories.remove("TFR")
    for cat in categories:
        total = sum(xlsx[cat]["Balance"])
        xlsx[cat]["Balance"].append(total)
        xlsx[cat]["Description"].append("Total")
        current_datetime = datetime.now()
        xlsx[cat]["Date"].append(current_datetime.strftime("%I:%M%p %a %-d %B, %Y").lower())
    # set total expense to be sum of balance columns of all sheets
    total = ""
    for cat in categories:
      total += f"+SUM('{cat}'!A:A)" # sum of sheet balance column 
    total = total.strip("+")
    total = "="+total
    xlsx["Total"]["Balance"].append(total)

    # write to xlsx if out is passed as arg
    if out:
        with pd.ExcelWriter('CATEGORISED_'+Path(fp).stem+'.xlsx') as writer:
            for cat in categories:
                pd_df = pd.DataFrame(xlsx[cat])
                pd_df.to_excel(writer, sheet_name=cat, index=False) # not sure about double braces here
            for cat in ["Total", "Unknown"]: # handle special cases
                pd_df = pd.DataFrame(xlsx[cat])
                pd_df.to_excel(writer,sheet_name=cat, index=False)

    # print(f"Categorisation complete! {df.size} total transactions were considered, { len(xlsx["Unknowned"]["description"])} of which were unable to be categorised.")
    return xlsx


# EXAMPLE'
result = main("/Users/timothyalder/Documents/tplat/projects/budget/docs/data/Transactions_2025-01-01_2025-01-22.csv", out=True)
import pandas as pd
import re
from typing import Union
from pathlib import Path

# keys dict provide a level of abstraction that will ensure the program can easily be made compatible with other banks csv formats.
keys = {"Description" : ["Long description"], "Balance" : ["Debit amount"], "Date": ["Create date"]} # if using a new bank bank with differnt csv format, add as value 
matches =  {"TFR": ["tfr from t j alder"], "Takeout": ["subway"], "Groceries": ["woolworths", "coles"], "Icecream":["spiltmilk"], "Petrol":["ampol", "bp", "7-eleven"], 
           "Physio":["woden integrated phy"], "Doctor":[], "Alcohol":["bws","liqourland"], "Dentist":[], 
           "Exercise":["club lime","dark carnival"], "Declined EFT":["declined eft fee"], "Car":["super cheap","bapcor"], 
           "Bunnings":["bunnings"], "Uber":["uber"], "Subscriptions":["remarkable"]}
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
        elif cat=="Unknown":
            xlsx["Unknown"]["Balance"].append(t.balance)
            xlsx["Unknown"]["Description"].append(t.description)
            xlsx["Unknown"]["Date"].append(t.date)
        else:
            xlsx[cat]["Balance"].append(t.balance)
            xlsx[cat]["Description"].append(t.description)
            xlsx[cat]["Date"].append(t.date)
        

    # set total expense to be sum of balance columns of all sheets
    categories.remove("TFR")
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
result = main("projects/budget/docs/data/Transactions_2022-12-01_2023-05-03.csv", out=True)
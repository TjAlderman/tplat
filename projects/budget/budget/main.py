import pandas as pd
import re

class TransactionCategoriser:
    """
    Class that is initialised using a .csv containing transaction history, and uses the description
    associated with each transaction to sort into a category.

    :param fp: Filepath to DefenceBank formatted .csv containing transaction history.
    :type fp: str
    """

    def __init__(self, fp: str):
        # Store the filepath
        self.fp = fp
        # Read in data
        self.df = pd.read_csv(fp, delimiter = ',')
        # Initialise categories
        self.categories = ["Subway", "Groceries", "Spilt Milk", "Petrol", 
                           "Physio", "Doctor", "Alcohol", "Dentist", 
                           "Dark Carnival", "Club Lime", "Declined EFT", "Car", 
                           "Bunnings", "Unknown", "Total"]
        # Initialise amounts
        self.amount = [0 for _ in range(len(self.categories))] 
        # Create dict to store results
        self.categorised = dict(zip(self.categories,self.amount))
        self.missed = 0 # count number of mixed transactions
        # Sort the data
        self.classify()

    def classify(self):
        # Add to the total
        for i in range(self.df['Long description'].size):
            self.categorised['Total'] += float(self.df['Debit amount'][i])
        # Sort into a category
        if re.search('Woolworths',self.df['Long description'][i]) or re.search('WOOLWORTHS',self.df['Long description'][i]) or (re.search('COLES', self.df['Long description'][i]) and not re.search('COLES EXPRESS', self.df['Long description'][i])):
            self.categorised['Groceries'] += float(self.df['Debit amount'][i])
        elif re.search('SUBWAY',self.df['Long description'][i]):
            self.categorised['Subway'] += float(self.df['Debit amount'][i])
        elif re.search('SPILTMILK',self.df['Long description'][i]):
            self.categorised['Spilt Milk'] += float(self.df['Debit amount'][i])
        elif re.search('AMPOL',self.df['Long description'][i]) or re.search('BP',self.df['Long description'][i]) or re.search('7-ELEVEN',self.df['Long description'][i]) or re.search('EG GROUP', self.df['Long description'][i]) or re.search('COLES EXPRESS', self.df['Long description'][i]):
            self.categorised['Petrol'] += float(self.df['Debit amount'][i])
        elif re.search('WODEN INTEGRATED PHY',self.df['Long description'][i]):
            self.categorised['Physio'] += float(self.df['Debit amount'][i])
        elif re.search('DARK CARNIVAL', self.df['Long description'][i]):
            self.categorised['Dark Carnival'] += float(self.df['Debit amount'][i])
        elif re.search('TFR from T J Alder', self.df['Long description'][i]):
            pass
        elif re.search('SUPER CHEAP',self.df['Long description'][i]) or re.search('BAPCOR',self.df['Long description'][i]):
            self.categorised['Car'] += float(self.df['Debit amount'][i])
        elif re.search('BWS',self.df['Long description'][i]) or re.search('LIQUORLAND',self.df['Long description'][i]):
            self.categorised['Alcohol'] += float(self.df['Debit amount'][i])
        elif re.search('Declined EFT Fee', self.df['Long description'][i]):
            self.categorised['Declined EFT'] += self.df['Debit amount'][i]
        elif re.search('BUNNING', self.df['Long description'][i]):
            self.categorised['Bunnings'] += self.df['Debit amount'][i]
        # Otherwise, add to missed 
        else:
            print(self.df['Long description'][i])
            self.categorised['Unknown'] += float(self.df['Debit amount'][i])
            self.missed += 1 

        print(f"Categorisation complete! {self.df.size} total transactions were considered, {self.missed} of which were unable to be categorised.")

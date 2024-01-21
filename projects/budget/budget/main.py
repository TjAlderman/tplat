import pandas as pd
import re
from typing import Union

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


    def sort(self, category: str, keywords: Union[str,list], index: str):
        """
        For the given index, check if the long description matches any of the provided keywords. If so,
        add the cost to the provided category

        :param category: Category to sort the transaction into, if identfied.
        :type category: str
        :param keywords: Keywords to check the long description for matches.
        :type keywords: Union[str,list]
        :param index: Index (transaction) to be processed.
        :type index: str
        """
        description = self.df['Long description'][index]
        if isinstance(keywords, list) and any(re.search(key, description) for key in keywords):
            self.categorised[category] += float(self.df['Debit amount'][index])
            return 1
        elif isinstance(keywords, str) and re.search(keywords, description):
            self.categorised[category] += float(self.df['Debit amount'][index])
            return 1
        return 0
        

    def classify(self):
        # Add to the total
        for index in range(self.df['Long description'].size):
            # get the data
            description = self.df['Long description'][index]
            amount = float(self.df['Debit amount'][index])
            # add to total
            self.categorised['Total'] += amount
            # sort into category
            found = 0
            while not found:
                
                found = self.sort('')

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

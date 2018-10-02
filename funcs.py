#!/usr/bin/env python
import pickle

def load_df():
    """ Helper function to load dataframe.
    
    Return: pd.DataFrame object
    """
    with open('data/df.pkl', 'rb') as pkl:
        pickled_df = pickle.load(pkl)

    return pickled_df

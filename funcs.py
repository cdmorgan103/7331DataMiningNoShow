#!/usr/bin/env python
import pickle

def load_df():
    """ Helper function to load dataframe.
    
    Return: pd.DataFrame object
    """
    with open('data/df.pkl', 'rb') as pkl:
        pickled_df = pickle.load(pkl)

    return pickled_df

def save_df(df):
    """ Helper function to save df (pd.DataFrame) as 'data/df.pkl'. """
    with open('data/df.pkl', 'wb') as pkl:
        pickle.dump(df, pkl)
import pandas as pd 
import numpy as np 

df = pd.read_csv('../data/ramen-ratings.csv')
target = 'Top Ten'

def wrangle_df(df):
    """
    This wrangle function counts null values and creates a train_test
    split based on your 'target' variable

    Before running this function, assign a column name to the variable "target"

    Params: a dataframe called "df"

    Outputs a tuple containing, in order, X, y, X_train, X_test, y_train, y_test
    
    """

    null_values = df.isnull().sum().sum()

    from sklearn.model_selection import train_test_split
    X = df.drop(columns=target)
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.2,
                                                        random_state=42)
    return(X, y, X_train, X_test, y_train, y_test)

print(wrangle_df(df))

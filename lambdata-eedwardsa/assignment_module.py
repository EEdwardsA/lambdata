import pandas as pd 
import numpy as np 
df = pd.read_csv("../data/archive/2019.csv")
target = 'Healthy life expectancy'
def wrangle_df(df):
    """This wrangle function counts null values and creates a train_test
    #split based on your 'target' variable"""

    print(f'The df contains', df.isnull.sum(), "null values")
    from sklearn.model_selection import train_test_split
    X = df.drop(columns=target)
    X_train, X_test, y_train, y_test = train_test_split(X, 
                                                        y, 
                                                        test_size=0.2, 
                                                        random_state=42)
    return(X_train, X_test, y_train, y_test)

wrangle_df(df)
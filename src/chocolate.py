import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

##count values and sort low to high (returns series)
def valcount_and_sort(column_name, df):
    column_name = df[column_name].value_counts().sort_index()
    return column_name



##sorts three columns by col2 high to low
def trivalue_sort(col1, col2, col3, df=chocbar_df):

    sorted_hivalues = df[[col1, col2, col3]].sort_values(col2, ascending=False)
    return sorted_hivalues



# Sort two columns in a dataframe

def two_sorted(cola,colb,df=chocbar_df):

    return df[[cola, colb]].sort_values(colb)



#Sum and sort two columns and reset the index

def sum_and_sort(cola, colb):
    top_man = (
    two_sorted(cola, colb)
    .groupby(cola)
    .sum()
    .sort_values(colb, ascending=False)
    )
    return top_man.reset_index()


#Take two series and make one
def add_two_lists(lista, listb):

    two_combined = lista.append(listb)
    return two_combined

if __name__ == "__main__":
    #Import csv as dataset
    chocbar_df = pd.read_csv("../data/chocolate_bars.csv")
    test_series = valcount_and_sort('year_reviewed',chocbar_df)
    print(test_series)

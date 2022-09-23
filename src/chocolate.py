import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

chocbar_df = pd.read_csv("../data/chocolate_bars.csv")


##count values and sort low to high (returns series)
def valcount_and_sort(column_name, df=chocbar_df):
   
    """
    Function that takes a column from a dataframe, counts the occurance
    of a value and sorts returning a series
    """
   
    column_name = df[column_name].value_counts().sort_index()
    return column_name




##sorts three columns by col2 high to low
def trivalue_sort(col1, col2, col3, df=chocbar_df):

    """
    Function that takes three seperate columns and sorts
    them by the second column to return a sorted dataset with the highest
    values on top
    """

    sorted_hivalues = df[[col1, col2, col3]].sort_values(col2, ascending=False)
    return sorted_hivalues




# Sort two columns in a dataframe

def two_sorted(cola,colb,df=chocbar_df):

    """
    Funtion that takes two columns (cola, colb) and sorts by colb
    returning sorted series with lowest values on top
    """

    return df[[cola, colb]].sort_values(colb)




#Sum and sort two columns and reset the index

def sum_and_sort(cola, colb):

    """
    Function that takes two columns sorts in to a series
    then takes the sorted series and adds the values of the second column
    and returns a new dataset with the highest values on top
    """

    top_man = (
    two_sorted(cola, colb)
    .groupby(cola)
    .sum()
    .sort_values(colb, ascending=False)
    )
    return top_man.reset_index()




#Take two series and make one
def add_two_lists(lista, listb):

    """
    Function that takes two series and returns one
    with the values combined
    """

    two_combined = lista.append(listb)
    return two_combined



def plot_summary(
    dfcola: pd.Series,
    dfcolb: pd.Series,
    fig_title: str,
    y_label: str
    )-> None:
    """
    Function for creating/showing a graph
    """


    fig, ax = plt.subplots()


    plt.barh(dfcola, dfcolb, color= ('saddlebrown'))
    plt.yticks(dfcola, horizontalalignment='right', fontsize='10')
    plt.ylabel(y_label)
    plt.xlabel("Rating")
    plt.title(fig_title)
    

    plt.show()

    



if __name__ == "__main__":
    #Import csv as dataset
    chocbar_df = pd.read_csv("../data/chocolate_bars.csv")
    test_series = valcount_and_sort('year_reviewed',chocbar_df)
    print(test_series)

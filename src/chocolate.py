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

    sorted_values = df[[col1, col2, col3]].sort_values(col2, ascending=False)
    return sorted_values




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

def hilo_rated_bar_pipeline():

    """
    Transform raw dataframe in to 10 highest rated chocolate bars dataset and
    10 lowest rated to graph
    """
    hi_ten = trivalue_sort('bar_name','rating', 'review').head(10)
    print(hi_ten)

    lo_ten = trivalue_sort('bar_name','rating', 'review').tail(10)
    lorated_graph = plot_summary(
        lo_ten['bar_name'],
        lo_ten['rating'],
        "Lowest Rated Chocolate Bar",
        "Chocolate Bar Name"
     )
    print(lorated_graph)

def hi_lo_manufac_pipeline():

    """
    Transform raw data to get the 10 highest and 10 lowest rated
    manufacturers by their cumulative rating to a series and show a graph
    """

    man_rated = two_sorted('manufacturer', 'rating')
    hi_man = sum_and_sort('manufacturer', 'rating').head(10)
    lo_man = sum_and_sort('manufacturer', 'rating').tail(10)
    hilo_man = add_two_lists(hi_man,lo_man)
    rated_man = plot_summary(
    hilo_man['manufacturer'],
    hilo_man['rating'],
    "Highest/Lowest Rated Chocolate Bar Manufacturer",
    "Manufacturer Name")
    print(rated_man)

def bean_origin_pipeline():

    """
    Filters raw data to to get highest 10 and lowest 10 rated bean origins to datasets
    reseting thier indexes and prints a graph
    """
    
    bean_rating = two_sorted('bean_origin', 'rating')
    top_bean = sum_and_sort('bean_origin', 'rating')
    hi_bean = top_bean.head(10).reset_index()
    lo_bean = top_bean.tail(10).reset_index()
    hilo_bean = add_two_lists(hi_bean,lo_bean)
    bean_rated = plot_summary(
    hilo_bean['bean_origin'],
    hilo_bean['rating'],
    "Where Do the Best Beans Originate?",
    "Bean Origin")
    print(bean_rated)



if __name__ == "__main__":
    """used to test functions"""
    #Import csv as dataset
    # chocbar_df = pd.read_csv("../data/chocolate_bars.csv")
    # test_series = valcount_and_sort('year_reviewed',chocbar_df)
    # print(test_series)
    # man_rated = two_sorted('manufacturer', 'rating')
    # lo_man = sum_and_sort('manufacturer', 'rating').tail(10)
    # plot_summary(
    # lo_man['manufacturer'],
    # lo_man['rating'],
    # 'Lowest Rated Bars',
    # "Manufacturer Name")
    # hilo_rated_bar_pipeline()
    # hi_lo_manufac_pipeline()
    # bean_origin_pipeline()
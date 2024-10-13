import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def find_outliers_iqr(df, column, width = 1.5):
    """
    Identifies outliers in a DataFrame column using the Interquartile Range (IQR) method.

    Parameters:
    - df (pandas.DataFrame): The DataFrame containing the data.
    - column (str): The name of the column in which to detect outliers.
    - width (float): The width of the IQR factor (default = 1.5)

    Returns:
    - pandas.DataFrame: A DataFrame containing the rows where outliers are present in the specified column.
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - width * IQR
    upper_bound = Q3 + width * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers


def check_columns(data):
    """
    Checks if all DataFrames in the given list have the same columns.

    Parameters:
    - data (list of pd.DataFrame): A list of pandas DataFrames to check for matching columns.

    Returns:
    - (bool): True if all DataFrames have the same columns, False otherwise.
    """

    cols = data[0].columns

    for df in data:
        if not all(df.columns == cols):
            return False
        
    return True



def cleaning_columns(df, name: str):
    """
    Cleans and renames columns in the dataframe by replacing code values with their corresponding names and adjusting the column structure.

    Parameters:
    - df (pd.DataFrame): The dataframe containing the columns with code and name information.
    - name (str): The prefix used to identify the columns ('Superior Agency', ,'Agency' or 'Managing Unit').

    Returns:
    - pd.DataFrame: The updated dataframe with the code column renamed and cleaned.
    """
    # We build a dataframe that gives us the code for every name. 
    # We have to group by Name, convert to a dataframe and keep the Name and Code
    df_aux = df[[f'{name} Code', f'{name} Name']].groupby(f'{name} Name').value_counts().reset_index()[[f'{name} Name', f'{name} Code']]

    # Now we store these columns in a dictionary to rename the codes
    dict_aux = dict(zip(df_aux[f'{name} Code'], df_aux[f'{name} Name']))

    # Replacement
    df[f'{name} Code'].replace(dict_aux, inplace = True)

    # For those values we reassign the name (only for NaN code and not NaN name)
    df.loc[df[f'{name} Code'].isna() & df[f'{name} Name'].notna(), f'{name} Code'] = df[f'{name} Name']

    df.rename(columns={f'{name} Code': f'{name}'}, inplace=True)
    df.drop(columns=[f"{name} Name"], inplace = True)

    return df


def time_evolution(df, name:str, scale = None):
    """
    Generates a time evolution plot for a given column in the provided DataFrame, using a log scale on the y-axis.

    Parameters:
    - df (DataFrame): The DataFrame containing the data for plotting.
    - name (str): The column name to be plotted on the y-axis.

    Returns:
    - None: Displays the time evolution plot.
    """
    plt.figure(figsize=(10, 4))

    sns.lineplot(x = 'Fiscal Year',
                y = name,
                hue = 'Economic Category',
                marker = 'o',
                linestyle = 'dashed',
                linewidth = 1,
                errorbar= None,
                palette='mako',
                data = df)

    if scale == 'log':
        plt.yscale('log')

    plt.legend(bbox_to_anchor=(1, 0.7))
    plt.title(f'{name} over time')
    plt.tight_layout()
    plt.show()


def box_plot(df, name:str, scale = None):
    """
    Generates a box plot to visualize the distribution of a specified column grouped by economic categories, with an optional log scale.

    Parameters:
    - df (DataFrame): The DataFrame containing the data for plotting.
    - name (str): The column name to be plotted on the y-axis.
    - scale (str, optional): The scale for the y-axis. If set to 'log', applies a logarithmic scale. Default is None.

    Returns:
    - None: Displays the box plot.
    """
    plt.figure(figsize = (7, 5))

    sns.boxplot(x = 'Economic Category',
                y = name,
                data = df,
                palette = 'mako'
                )

    plt.xticks(rotation = 30)

    if scale == 'log':
        plt.yscale('log')

    plt.title(f'Distribution of {name} per category')
    plt.ylabel('Amount (BRL)')
    plt.tight_layout()
    plt.show()
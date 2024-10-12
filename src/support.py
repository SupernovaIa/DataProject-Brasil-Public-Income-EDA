import pandas as pd
import numpy as np

def find_outliers_iqr(df, column):
    """
    Identifies outliers in a DataFrame column using the Interquartile Range (IQR) method.

    Parameters:
    - df (pandas.DataFrame): The DataFrame containing the data.
    - column (str): The name of the column in which to detect outliers.

    Returns:
    - pandas.DataFrame: A DataFrame containing the rows where outliers are present in the specified column.
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers
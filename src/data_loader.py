"""
    CSV Reader:
        Load CSV
        Read CSV
        Load CSV price data into a pandas DataFrame
        Convert the date column properly
        Sort it
        Return cleaned result
    
    """

"""
    Questions:
        What exactly is a CSV
            - a 'Comma-Separated Values' plain text file (.csv)
            - stores data in rows and columns separated by a comma - each line (record), separated commas (fields)

        What library do you use to read the CSV
            - Pandas does the reading and manipulating

        What is a pandas DataFrame - what does it look like?
            - 2 dimensional data structure (array or table with rows and columns):
            - See example below

        How does the computer utilise the CSV - does it read it? Sort it?
            - Reads it, sorts it, cleans it - All through pandas functions

        What is the exact input of data?
            - 

        What is the exact output of data that can be utilised in further functions?
            - the output of read_csv is fine

        Do I need to establish a class?
            - 

        Do I need to do all these steps in multiple functions?
            - 
        
    """

# Initialise libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# System Confirmation
# print("Environment is working.")
# print("Pandas version:", pd.__version__)
# print("NumPy version:", np.__version__)


filler_csv = r'C:\Users\olive\OneDrive\Desktop\filler.csv'

# df_loc = input('Please input file location: ')

# Input and read the CSV
def read_csv_data(file_path):
    df_loc = file_path
    df = rf'{df_loc}'
    df_read = pd.read_csv(df)
    return df_read

# Function to clean the CSV input
#    Currently: reformats 'Date', drops duplicates, drops Na values
#    Potentially: flag outliers, remove characters that prevent numeric parsing ($, %, & etc.)
def clean_csv_data(df):
    read_df = df
    read_df['Date'] = pd.to_datetime(read_df['Date'], format='mixed')
    read_df.drop_duplicates(inplace = True)
    cleaned_CSV = read_df.dropna()
    return cleaned_CSV

# Filler function to detect outliers
#   Must determine how to actually detect outliers based of specific parameters for the values, and also which values to search through
#       Merely test function:
def detect_outliers(df):
    for value in df.index:
        if df.loc[value, 'High'] > 2000:
            df.drop(value, inplace=True)
    return df

print(clean_csv_data(r'C:\Users\olive\OneDrive\Desktop\filler.csv'))
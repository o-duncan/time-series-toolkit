# Initialise libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Input and read the CSV

def read_csv_data(file_path):
    """
    - Take file path and read input
    - Output read CSV in a pandas dataframe

    """

    df = pd.read_csv(file_path)
    return df

# Function to clean the CSV input
#    Currently: reformats 'Date', drops duplicates, drops Na values
#    Potentially: flag outliers, remove characters that prevent numeric parsing ($, %, & etc.)

def clean_csv_data(df):
    """
    - Copy original CSV input - won't modify original file
    - Convert 'Date' into standardised datetime formatting - reformat invalid date entries into NaT
    - Drop duplicates
    - Sort by Date
    - Remove empty columns to ensure smooth parsing
    - Set index as Date

    """
    cleaned_df = df.copy()

    cleaned_df['Date'] = pd.to_datetime(cleaned_df['Date'], errors='coerce')

    cleaned_df.drop_duplicates(inplace = True)

    cleaned_df = cleaned_df.sort_values('Date')

    cleaned_df = cleaned_df.dropna()

    cleaned_df.set_index('Date', inplace=True)

    return cleaned_df


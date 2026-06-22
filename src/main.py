import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

from data_loader import read_csv_data, clean_csv_data

"""
print("Environment is working.")
print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)
"""



filler_csv = r'C:\Users\Thomas Duncan\Projects\time-series-toolkit\data\filler.csv'

read_df = read_csv_data(filler_csv)
print(clean_csv_data(read_df))


def main():
    
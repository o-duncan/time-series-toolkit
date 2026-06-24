import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
from pathlib import Path

from data_loader import read_csv_data, clean_csv_data
from metrics import calculate_simple_returns


# Form project root and file directory
 
project_root = Path(__file__).parent.parent
file_path = project_root / 'data' / 'filler.csv'


def main():
    """
    - Input data set
    - Create raw dataframe
    - Create cleaned df
    - Create a Series of simple returns
    """

    raw_df = read_csv_data(file_path)
    cleaned_df = clean_csv_data(raw_df)
    simple_returns = calculate_simple_returns(cleaned_df)

    cleaned_df.info()
    print()
    print(simple_returns)



if __name__ == '__main__':
    main()

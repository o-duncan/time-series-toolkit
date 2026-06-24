import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
from pathlib import Path

from data_loader import read_csv_data, clean_csv_data


# Form project root and file directory
 
project_root = Path(__file__).parent.parent
file_path = project_root / 'data' / 'filler.csv'


def main():
    """
    - Input data set
    - Create raw dataframe
    - Create cleaned df
    - Output a confirmation of cleaned df as info
    """

    raw_df = read_csv_data(file_path)
    cleaned_df = clean_csv_data(raw_df)

    print(cleaned_df.info())



if __name__ == '__main__':
    main()

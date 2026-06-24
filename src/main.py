import pandas as pd
import numpy as np

from pathlib import Path

from data_loader import read_csv_data, clean_csv_data
from metrics import calculate_simple_returns, calculate_log_returns, calculate_rolling_volatility, calculate_moving_average, calculate_drawdowns


# Form project root and file directory
 
project_root = Path(__file__).parent.parent
file_path = project_root / 'data' / 'filler.csv'


def main():
    """
    - Input data set
    - Create raw dataframe
    - Create cleaned df
    - Create a Series of simple returns
    - Create a Series of log returns
    """

    raw_df = read_csv_data(file_path)
    cleaned_df = clean_csv_data(raw_df)

    simple_returns = calculate_simple_returns(cleaned_df)
    log_returns = calculate_log_returns(cleaned_df)

    rolling_volatility = calculate_rolling_volatility(cleaned_df)
    moving_averages = calculate_moving_average(cleaned_df)

    drawdowns = calculate_drawdowns(cleaned_df)

    cleaned_df.info()
    print()
    print(drawdowns)


if __name__ == '__main__':
    main()

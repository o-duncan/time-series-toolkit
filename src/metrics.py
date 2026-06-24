import pandas as pd
import numpy as np
from pathlib import Path

# Calulating daily simple returns, outputing a Series of daily percentage pricing changes

def calculate_simple_returns(cleaned_df, price_column='Close'):
    """
    - Input a cleaned dataframe
    - Convert prices to pd Series
    - Default to analysing 'Close' column - however allow variations to be accepted
    - Utilise pd percentage change to convert pricing into simple returns
    - Output as Series, indexed by date

    """

    prices_series = cleaned_df[price_column]

    simple_returns_series = prices_series.pct_change()

    return simple_returns_series


# Calculate daily log returns

def calculate_log_returns(cleaned_df, price_column='Close'):
    """
    - Input cleaned dataframe
    - convert prices to pd Series
    - Default to 'Close' prices unless specified
    - Take difference of log values of prices between days
    - Return a Series of log returns
    """

    prices_series = cleaned_df[price_column]

    log_returns_series = np.log(prices_series).diff()

    return log_returns_series



import pandas as pd
import numpy as np
from pathlib import Path


# Calulating simple daily returns, outputing a Series of daily percentage pricing changes

def calculate_simple_returns(cleaned_df, price_column='Close'):
    """
    - Input a cleaned dataframe
    - Convert prices to pd Series with date index
    - Default to analysing 'Close' column - however allow variations to be accepted
    - Utilise pd percentage change to convert pricing into simple returns
    - Output as a one-dimensional Series, indexed by date

    """

    returns_series = cleaned_df[price_column]

    simple_returns_series = returns_series.pct_change()

    return simple_returns_series



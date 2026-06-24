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


# Calculate rolling volatility

def calculate_rolling_volatility(cleaned_df, price_column='Close'):
    """
    - Input cleaned dataframe into function
    - Calculate log returns from each day
    - Calculate the standard deviation of the trailing 20 daily log returns for each date
    - Annualise the volatility
    - Output rolling volatility series

    - Assuming 20 trading days per month, 252 trading days per year
    """

    log_returns = calculate_log_returns(cleaned_df[price_column])

    std_series = log_returns.rolling(window=20).std()

    rolling_volatility_series = std_series * np.sqrt(252)

    return rolling_volatility_series

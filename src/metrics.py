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

def calculate_rolling_volatility(cleaned_df, price_column='Close', window_size=20, trading_days_per_year=252):
    """
    - Input cleaned dataframe into function
    - Calculate log returns from each day
    - Calculate the standard deviation of the trailing 20 daily log returns for each date
    - Annualise the volatility
    - Output rolling volatility series

    - Assuming 20 trading days per month, 252 trading days per year
    """

    log_returns = calculate_log_returns(cleaned_df, price_column)

    std_series = log_returns.rolling(window=window_size).std()

    rolling_volatility_series = std_series * np.sqrt(trading_days_per_year)

    return rolling_volatility_series


# Calculating moving averages

def calculate_moving_average(cleaned_df, price_column='Close', window_size=20):
    """
    - Input cleaned dataframe
    - calculate the rolling mean of data with configurable window size
    
    - Default window size of 20, assuming 20 trading days per month
    """

    pricing_series = cleaned_df[price_column]

    rolling_average_series = pricing_series.rolling(window=window_size).mean()

    return rolling_average_series



# Calculate drawdowns

def calculate_drawdowns(cleaned_df, price_column='Close'):
    """
    - Input cleaned dataframe
    - Take the Series of the simple returns
    - Create a Series of cumulative returns for each day
    - Find each respective previous max
    - Output Series of drawdowns
    """

    simple_returns_series = calculate_simple_returns(cleaned_df, price_column)

    cumulative_returns = (1 + simple_returns_series).cumprod()

    cumulative_max = cumulative_returns.cummax()

    drawdowns_series = (cumulative_returns - cumulative_max) / cumulative_max

    return drawdowns_series



# General Statistics Summary function

def calculate_summary_statistics(cleaned_df, price_column='Close', trading_days_per_year=252):
    """
    - Create a price series from an inputted cleaned dataframe
    - Create a function to determine the observation count of the dataset
    - Calculate start price and end price
    - Calcualte cumulative returns from the chosen pricing column
    - Calculate the annualised volatility of the data set
    - Find the maximum drawdown of the pricing history
    - Output this is as a summary of respective statistics
    """
    
    price_series = cleaned_df[price_column]

    observation_count = price_series.count()

    start_price = price_series.iloc[0]
    end_price = price_series.iloc[-1]

    cumulative_return = (end_price - start_price) / start_price

    annualised_volatility = calculate_log_returns(cleaned_df, price_column).std() * np.sqrt(trading_days_per_year)

    maximum_drawdown = calculate_drawdowns(cleaned_df, price_column).min()
    

    summary_list = [observation_count, start_price, end_price, cumulative_return, annualised_volatility, maximum_drawdown]
    summary_titles = [
        'Observation count:', 
        'Starting price:', 
        'Ending price:', 
        'Cumulative return:', 
        'Annualised Volatility:', 
        'Maximum drawdown:'
        ]
    
    summary_series = pd.Series(summary_list, index=summary_titles)
    return summary_series
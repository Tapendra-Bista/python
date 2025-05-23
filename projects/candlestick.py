import yfinance as yf
import mplfinance as mpf
import pandas as pd

ticker = input("Enter the stock name: ")
try:
    df = yf.download(ticker, start='2023-08-01', end='2024-09-01')

    if df.empty:
        print(f"No data found for ticker {ticker} within the specified date range.")
    else:
        # Attempt to convert all columns to numeric types
        for col in df.columns:
            try:
                df[col] = pd.to_numeric(df[col])
            except ValueError:
                print(f"Could not convert column '{col}' to numeric. Skipping.")
                #Option 1: Remove the column
                df = df.drop(col, axis=1)
                #Option 2: Fill with a default value
                #df[col] = df[col].fillna(0) #Fills non-numeric with 0

        #Check if required columns exist after conversion attempt
        required_columns = ['Open', 'High', 'Low', 'Close']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"Missing required columns: {missing_columns}. Cannot plot candlestick chart.")
        else:
            mpf.plot(df, type='candle', style='charles', title=f'{ticker} Candlestick chart', ylabel='Price')

except ValueError as e:
    print(f"ValueError: {e}")
    print("Check the date format. It should be YYYY-MM-DD.")
except Exception as e:
    print(f"An error occurred: {e}")
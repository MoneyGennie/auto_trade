from broker_connector.connector import connector
from historic_data_storage.historic_data_store import get_data_store, release_data_store
from indicators.superTrend import SuperTrend
from strategies.supertrend_options import generate_trade_signal
from execution.execution_manager_buy import TradingAutomation

import os
from dotenv import load_dotenv
import yfinance as yf
import pandas as pd
from pandas.tseries.offsets import BDay
from datetime import datetime, timedelta

# Load environment variables from .env file
load_dotenv()


# For temp
intraday_df = ''

security_id = '25'
exchange_segment = 'IDX_I'
instrument_type = 'INDEX'
period = 10
multiplier = 2
symbol = 'BANKNIFTY'


def connect_broker():
    client_id = os.environ['CLIENT_ID']
    order_key = os.environ['ORDER_KEY']
    data_key = os.environ['DATA_KEY']
    broker = connector(client_id, order_key, data_key)
    data_dhan = broker.data_api_connect()
    order_dhan = broker.order_api_connect()
    return data_dhan, order_dhan

def save_old_data():
    # Define the ticker symbol
    ticker_symbol = "^NSEBANK"  # Use ".BO" for BSE or ".NS" for NSE

    # Get today's date
    end_date = datetime.today().strftime('%Y-%m-%d')

    # Find the last working day
    last_working_day = pd.Timestamp(end_date) - BDay(1)  # BDay from pandas is used to find the last business day
    last_working_day = last_working_day.strftime('%Y-%m-%d')

    # Calculate the start date (1 month before the last working day)
    start_date = (pd.Timestamp(last_working_day) - pd.DateOffset(months=1)).strftime('%Y-%m-%d')

    # Fetch historical data
    banknifty = yf.download(ticker_symbol, start=start_date, end=end_date, interval="15m")
    # banknifty.rename(columns = {'Datetime': 'date'}, inplace = True) 
    banknifty.index = banknifty.index.rename('date')

    banknifty.to_csv("BN15min.csv")


def main():
    save_old_data()
    data_dhan, order_dhan = connect_broker()
    # print(order_dhan)
    # print(order_dhan.get_fund_limits())
    # print(order_dhan.get_positions())
    t = TradingAutomation(order_dhan, data_dhan, security_id, exchange_segment, instrument_type, period, multiplier)
    t.schedule_execution()

    # option_security_id = symbolGenerator().construct_supertrend_symbol(
    #     symbol, intraday_df[f'ST_{period}_{multiplier}'].iloc[-2], intraday_df["date"].iloc[-1], signal)
    # print(option_security_id)
    # print(historic_df.tail())
    # release_data_store(symbol)



# main function
if __name__ == '__main__':
    main()

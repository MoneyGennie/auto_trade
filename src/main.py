from broker_connector.connector import connector
from historic_data_storage.historic_data_store import get_data_store, release_data_store
from indicators.superTrend import SuperTrend
from strategies.supertrend_options import generate_trade_signal
from execution.execution_manager import TradingAutomation


# For temp
intraday_df = ''

security_id = '25'
exchange_segment = 'IDX_I'
instrument_type = 'INDEX'
period = 10
multiplier = 2
symbol = 'BANKNIFTY'


def connect_broker():
    client_id = "1102077241"  # os.getenv('CLIENT_ID')
    # os.getenv('ORDER_KEY')
    order_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzA2OTY1Nzc0LCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMjA3NzI0MSJ9.h-rgLcsq0qILq83BFXKMItM801ylZC4NOExqKl_QfvKToDoKwYppuiAsfActpBTu1ANweE0Tqd_-lGzzeiLOwg"
    # os.getenv('DATA_KEY')
    data_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzA3MDY1NDE5LCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMjA3NzI0MSJ9.2RGM4-MrQGuhKf5EEZhE-1QreCvlecVLqXJFizp9PbQJQXjeB3Mtadxtpc3DD2hxyMb8SVQq5J8gZqaU6Si7Hw"
    broker = connector(client_id, order_key, data_key)
    data_dhan = broker.data_api_connect()
    order_dhan = broker.order_api_connect()
    return data_dhan, order_dhan


def main():
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

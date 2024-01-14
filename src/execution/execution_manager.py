from datetime import datetime, time
import time as sleep_time
import sys
from indicators.superTrend import SuperTrend
from strategies.supertrend_options import generate_trade_signal  
from .punch_order import OrderExecution  
from data_collector.intraday_data_colletor import intradayDataCollector
from symbols.symbols import symbol_generator




class TradingAutomation:
    def __init__(self,order_dhan, data_dhan, security_id, exchange_segment, instrument_type, period, multiplier):
        # Initialize your class variables or any setup required
        # self.intraday_df = intraday_df
        self.symbol = 'BANKNIFTY'
        self.security_id = security_id
        self.exchange_segment = exchange_segment
        self.instrument_type = instrument_type
        self.period = period
        self.multiplier = multiplier
        self.data_dhan = data_dhan
        self.order_dhan = order_dhan
        self.data_collector_obj = intradayDataCollector(data_dhan, security_id, exchange_segment, instrument_type)
        self.dhan_order_obj = OrderExecution(order_dhan)
        self.symbol_generator_obj = symbol_generator()


    def run_strategy(self):
        print("calling strategy now")
        self.intraday_df = self.data_collector_obj.get_intraday_data()
        self.df = SuperTrend(self.intraday_df, self.period, self.multiplier)
        self.df.to_csv("supertrend.csv", index= False)
        trade_signal = generate_trade_signal(self.df, self.period, self.multiplier)
        # Execute actions based on the trade signal (PUT, CALL, hold)
        if trade_signal == "PUT":
            self.strike_price = self.df.iloc[-1]['open']
            self.date_today = datetime.now().date()
            self.formatted_date = self.date_today.strftime("%d/%m/%Y")
            self.security_id = self.symbol_generator_obj.construct_supertrend_symbol (self.symbol, self.strike_price, self.formatted_date, trade_signal )
            self.dhan_order_obj.execute_put(self.security_id)
        elif trade_signal == "CALL":
            self.strike_price = self.df.iloc[-1]['open']
            self.date_today = datetime.now().date()
            self.formatted_date = self.date_today.strftime("%d/%m/%Y")
            print(self.date_today)
            self.security_id = self.symbol_generator_obj.construct_supertrend_symbol (self.symbol, self.strike_price, self.formatted_date, trade_signal )
            self.dhan_order_obj.execute_call(self.security_id)
        elif trade_signal == "hold":
            self.strike_price = self.df.iloc[-1]['open']
            self.date_today = datetime.now().date()
            self.formatted_date = self.date_today.strftime("%d/%m/%Y")
            self.dhan_order_obj.execute_hold()

    def schedule_execution(self):
        while True:
            current_time = datetime.now().time()
            print(current_time)
            # Check if the current time is between 9:30 AM and 3:30 PM
            market_open = time(9, 15)
            market_close = time(15, 30)

            if market_open <= current_time <= market_close:
                # Calculate the time remaining until the start of the next 15-minute interval
                time_until_next_interval = 15 - (current_time.minute % 15)

                # Sleep until the start of the next 15-minute interval
                sleep_seconds = (time_until_next_interval * 60) # Add 10 seconds to make sure we are past the current minute
                sleep_time.sleep(sleep_seconds)

                # Execute the strategy
                self.run_strategy()

            else:
                if current_time > market_close:
                    self.intraday_df = self.data_collector_obj.get_intraday_data()
                    self.intraday_df.to_csv("BN15min.csv", index=False)
                    print("Market is closed. Exiting.")
                    sys.exit()  # Terminate the program gracefully
                else:
                    print("Market is closed. Exiting.")
                    sys.exit()  # Terminate the program gracefully
import pandas as pd
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings("ignore")


class intradayDataCollector():
    def __init__(self, data_dhan, security_id, exchange_segment, instrument_type) -> None:
        self.security_id = security_id
        self.exchange_segment = exchange_segment
        self.instrument_type = instrument_type
        self.data_dhan = data_dhan

    def get_intraday_data(self):
        intraday_data = self.data_dhan.intraday_daily_minute_charts(
            self.security_id,
            self.exchange_segment,
            self.instrument_type
        )
        if intraday_data['status'] == 'failure':
            print("Intraday Data Not Available at This Moment")
            exit()
        else:
            intraday_data = pd.DataFrame(intraday_data['data'])
            intraday_data.columns = intraday_data.columns.str.lower()
            intraday_data.rename(columns={'start_time': 'date'}, inplace=True)


            intraday_data['date'] = intraday_data['date'].apply(self.data_dhan.convert_to_date_time)
            #reoder columns to match previous days column sequence 
            intraday_data = intraday_data[['date', 'open', 'high', 'low', 'close', 'volume']]
            # Get today's date and format it as a string
            today_date_str = datetime.now().date()

            # Create the target string with today's date
            target_date_str = f"{today_date_str} 15:30:00"


            # Convert the 'date' column to datetime
            intraday_data['date'] = pd.to_datetime(intraday_data['date'])

            # Identify the index of the last row with 'date' equal to the target date
            last_row_index = intraday_data[intraday_data['date'] == target_date_str].index

            # Drop the last row by index
            intraday_data.drop(last_row_index, inplace=True)

            new_rows = self.convert_to_15min(intraday_data)
            previous_days_data = pd.read_csv('BN15min.csv')
            previous_days_data.columns = previous_days_data.columns.str.lower()
            intraday_data.set_index('date', inplace=True)
            if previous_days_data.iloc[-1]['date'] != new_rows.iloc[-1]['date']:
                complete_data = pd.concat([previous_days_data, new_rows], ignore_index=True)
            else:
                complete_data = previous_days_data
            return complete_data

    def convert_to_15min(self, df):
        if len(df) >= 15:
            df.to_csv("input_data.csv", index=False)

            # Group by every 15 rows
            grouped_data = df.groupby(df.index // 15)

            # Create a new DataFrame for the aggregated results
            result_data = pd.DataFrame(columns=['date', 'open', 'high', 'low', 'close', 'volume'])

            # Iterate through each group
            for _, group in grouped_data:
                result_data = pd.concat([
                    result_data,
                    pd.DataFrame({
                        'date': [group['date'].iloc[0]],
                        'open': [group['open'].iloc[0]],
                        'high': [group['high'].max()],
                        'low': [group['low'].min()],
                        'close': [group['close'].iloc[-1]],
                        'volume': [group['volume'].sum()]
                    })
                ])
            

            result_data.to_csv("my_logic.csv",  index=False)
        return result_data

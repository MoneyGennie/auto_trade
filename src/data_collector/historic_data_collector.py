import pandas as pd


class historicDataCollector():
    def __init__(self, data_dhan, symbol, exchange_segment, instrument_type, expiry_code, from_date, to_date) -> None:
        self.symbol = symbol
        self.exchange_segment = exchange_segment
        self.instrument_type = instrument_type
        self.expiry_code = expiry_code
        self.from_date = from_date
        self.to_date = to_date
        self.data_dhan = data_dhan

    def get_historic_data(self):
        historic_data = self.data_dhan.historical_minute_charts(
            self.symbol,
            self.exchange_segment,
            self.instrument_type,
            self.expiry_code,
            self.from_date,
            self.to_date
        )
        for i in range(len(historic_data['data']['start_Time'])):
            historic_data['data']['start_Time'][i] = self.data_dhan.convert_to_date_time(
                historic_data['data']['start_Time'][i])
        print(historic_data)
        return pd.DataFrame(historic_data['data'])

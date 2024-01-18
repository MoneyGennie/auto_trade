from datetime import datetime, timedelta
import pandas as pd


class symbol_generator:
    def __init__(self) -> None:
        # 03/01/2024
        # create date object for date 03/01/2024
        week1_date = "03/01/2024"
        week2_date = "10/01/2024"
        week3_date = "17/01/2024"
        week4_date = "25/01/2024"
        week5_date = "31/01/2024"
        self.week1 = datetime.strptime(week1_date, "%d/%m/%Y").date()
        self.week2 = datetime.strptime(week2_date, "%d/%m/%Y").date()
        self.week3 = datetime.strptime(week3_date, "%d/%m/%Y").date()
        self.week4 = datetime.strptime(week4_date, "%d/%m/%Y").date()
        self.week5 = datetime.strptime(week5_date, "%d/%m/%Y").date()

    def get_expiry_date(self, date):
        date_obj = datetime.strptime(date, "%d/%m/%Y").date()
        if date_obj < self.week1:
            return self.week1
        elif date_obj < self.week2:
            return self.week2
        elif date_obj < self.week3:
            return self.week3
        elif date_obj < self.week4:
            return self.week4
        elif date_obj < self.week5:
            return self.week5
        else:
            return None

    def construct_supertrend_symbol(self, symbol, strike, date, signal):
        if not signal == 'hold':
            # read api-script-master.csv file
            all_scripts = pd.read_csv('api-scrip-master.csv')
            expiry_date = self.get_expiry_date(date)
            # BANKNIFTY 25 JAN 48000 PUT
            search_key = symbol + ' ' + \
                expiry_date.strftime("%d") + ' ' + \
                expiry_date.strftime("%b").upper() + ' ' + \
                str(round(strike, -2)).split('.')[0] + ' ' + signal
            print(search_key)
            # search for symbol in the file
            symbol_df = all_scripts[all_scripts['SEM_CUSTOM_SYMBOL'] == search_key]
            security_id = symbol_df['SEM_SMST_SECURITY_ID'].iloc[0]
            return security_id

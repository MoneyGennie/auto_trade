import yfinance as yf
import pandas as pd

class TechnicalScanner:
    def __init__(self) -> None:
        self.nifty_500_symbol = pd.read_csv(r"src\technical_scanners\nifty_500.csv")['Symbol']
        self.yahoo_500_symbol = self.nifty_500_symbol + ".NS"

    def get_high_and_today_close(self, symbol):
        # Download historical data for the given symbol from inception
        data = yf.Ticker(symbol).history(period='max')

        # Find the maximum closing price in the historical data
        high_price = data['High'].iloc[:-2].max()

        # Get today's closing price
        today_close = data['Close'].iloc[-1]

        return high_price, today_close

def main():
    scanner = TechnicalScanner()
    with open("all_time_high_list.txt", "w") as txt:


        for symbol in scanner.yahoo_500_symbol:
            try:
                high_price, today_close = scanner.get_high_and_today_close(symbol)
                
                if today_close > high_price:
                    # print(f"{symbol}: Today's close ({today_close}) is greater than the all-time high ({high_price})")
                    txt.write(f"{symbol}: Today's close ({today_close}) is greater than the the all-time high ({high_price})")
                # else:
                #     print(f"{symbol}: Today's close ({today_close}) is not greater than the all-time high ({high_price})")

            except Exception as e:
                print(f"Error processing {symbol}: {str(e)}")

if __name__ == "__main__":
    main()

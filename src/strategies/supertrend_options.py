def generate_trade_signal(df, period, multiplier):
    if df[f'STX_{period}_{multiplier}'].iloc[-1] == "up" and df[f'STX_{period}_{multiplier}'].iloc[-2] == "down":
        return "PUT"
    elif df[f'STX_{period}_{multiplier}'].iloc[-1] == "down" and df[f'STX_{period}_{multiplier}'].iloc[-2] == "up":
        return "CALL"
    else:
        return "hold"

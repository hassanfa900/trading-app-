import pandas as pd
import pandas_ta as ta

def calculate_indicators(df: pd.DataFrame):
    """
    df يجب أن يحتوي على الأعمدة: open, high, low, close, volume
    """
    df["EMA9"] = ta.ema(df["close"], length=9)
    df["EMA50"] = ta.ema(df["close"], length=50)
    df["EMA200"] = ta.ema(df["close"], length=200)
    df["RSI"] = ta.rsi(df["close"], length=14)
    df["MACD"], df["MACD_signal"] = ta.macd(df["close"], fast=12, slow=26, signal=9)[["MACD_12_26_9", "MACDs_12_26_9"]].T.values
    return df


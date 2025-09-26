def generate_signal(df_row):
    """
    يستقبل آخر صف (آخر شمعة) ويحدد الدخول أو الخروج
    """
    close = df_row["close"]
    ema50 = df_row["EMA50"]
    ema200 = df_row["EMA200"]
    rsi = df_row["RSI"]
    macd = df_row["MACD"]
    macd_signal = df_row["MACD_signal"]

    # قاعدة صلبة للدخول
    if close > ema50 and close > ema200 and macd > macd_signal and 40 <= rsi <= 60:
        return "BUY"

    # قاعدة صلبة للخروج
    if rsi > 70 or close < ema50 or macd < macd_signal:
        return "SELL"

    return "HOLD"


from collections import defaultdict

# تخزين البيانات في الذاكرة
candles_store = defaultdict(list)   # symbol -> list of candles
signals_store = []                  # list of Signal dicts


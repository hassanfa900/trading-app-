from pydantic import BaseModel

class Candle(BaseModel):
    time: str
    open: float
    high: float
    low: float
    close: float
    volume: float

class Signal(BaseModel):
    symbol: str
    action: str  # BUY / SELL / HOLD
    price: float
    timestamp: str


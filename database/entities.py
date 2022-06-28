from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Cripto(Base):

    __tablename__ = "criptos"

    id = Column(Integer, primary_key=True)
    symbol = Column(String(100), nullable=False, index=True)
    priceChange = Column(String(100), nullable=False)
    priceChangePercent = Column(String(100), nullable=False)
    weightedAvgPrice = Column(String(100), nullable=False)
    prevClosePrice = Column(String(100), nullable=False)
    lastPrice = Column(String(100), nullable=False)
    lastQty = Column(String(100), nullable=False)
    bidPrice = Column(String(100), nullable=False)
    bidQty = Column(String(100), nullable=False)
    askPrice = Column(String(100), nullable=False)
    askQty = Column(String(100), nullable=False)
    openPrice = Column(String(100), nullable=False)
    highPrice = Column(String(100), nullable=False)
    lowPrice = Column(String(100), nullable=False)
    volume = Column(String(100), nullable=False)
    quoteVolume = Column(String(100), nullable=False)
    openTime = Column(String(100), nullable=False)
    closeTime = Column(String(100), nullable=False)
    firstId = Column(String(100), nullable=False)
    lastId = Column(String(100), nullable=False)
    count = Column(String(100), nullable=False)
    time = Column(String(100), nullable=False)
    rise = Column(String(100), nullable=False)

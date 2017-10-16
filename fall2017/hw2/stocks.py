import csv
import datetime as dt
import sys

class Company:
    def __init__(self, symbol, name=None, sector=None):
        self.symbol = symbol
        self.name = name
        self.sector = sector
        self.stock_data = {}

    def __str__(self):
        return f"{self.name} ({self.symbol})"

    def __repr__(self):
        return f"<Company: name={self.name}, symbol={self.symbol}, sector={self.sector}>"

    def performance(self, start_date=None, end_date=None):
        start = self.stock_data[self.find_start(start_date)] \
                if start_date else self.stock_data[min(self.stock_data.keys())]
        end = self.stock_data[self.find_end(end_date)] \
              if end_date else self.stock_data[max(self.stock_data.keys())]
        return (end.adj_close - start.open_price) / start.open_price

    def find_start(self, date):
        for d in sorted(self.stock_data.keys()):
            if d.date() >= date.date():
                return d
        return None

    def find_end(self, date):
        for d in sorted(self.stock_data.keys(), reverse=True):
            if d.date() <= date.date():
                return d
        return None

class StockData:

    def __init__(self, open_price, high, low, close, adj_close, volume):
        self.open_price = open_price
        self.high = high
        self.low = low
        self.close = close
        self.adj_close = adj_close
        self.volume = volume
        performance = (adj_close - open_price) / open_price

    def _lt__(self, other):
        return self.adj_close < other.adj_close

if __name__=='__main__':
    company = Company(sys.argv[1])
    start = dt.datetime.strptime(sys.argv[2], "%Y-%m-%d") \
            if len(sys.argv) > 2 else None
    end = dt.datetime.strptime(sys.argv[3], "%Y-%m-%d") \
          if len(sys.argv) > 3 else None
    with open(f"{sys.argv[1]}.csv", "rt") as fin:
        for record in csv.DictReader(fin):
            date = dt.datetime.strptime(record['Date'], "%Y-%m-%d")
            company.stock_data[date] = StockData(float(record['Open']),
                                                 float(record['High']),
                                                 float(record['Low']),
                                                 float(record['Close']),
                                                 float(record['Adj Close']),
                                                 int(record['Volume']))
    start = start if start else min(company.stock_data.keys())
    end = end if end else max(company.stock_data.keys())
    perf = company.performance(start, end) * 100
    print(f"Stock performance of {company} from {start.date()} to {end.date()}: {perf:.1f}%.")

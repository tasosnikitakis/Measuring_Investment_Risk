import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime as dt
import ta
class Portfolio:
    def __init__(self):
        self.tickers = []
        self.num_shares = []
        self.weights = []
        self.prices = []
        self.values = []

    def add_stock(self, ticker, num_shares):
        self.tickers.append(ticker)
        self.num_shares.append(num_shares)

        # Get price data from Yahoo Finance
        ticker_data = yf.Ticker(ticker)
        ticker_price = ticker_data.history(period='1d')['Close'][0]
        self.prices.append(ticker_price)

        # Calculate weight and value of position
        portfolio_value = sum(self.prices[i] * self.num_shares[i] for i in range(len(self.tickers)))
        position_value = ticker_price * num_shares
        self.values.append(position_value)
        self.weights = [p * n / portfolio_value for p, n in zip(self.prices, self.num_shares)]

    def display(self):
        data = {'Ticker': self.tickers,
                'Shares': self.num_shares,
                'Weight': [f"{w * 100:.2f}%" for w in self.weights],
                'Price': self.prices,
                'Value': self.values}
        df = pd.DataFrame(data)
        print(df)

    def plot_pie_chart(self):
        labels = self.tickers
        sizes = self.weights
        explode = [0.1] * len(labels)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show()


    def yearly_candlestick_chart(self, ticker):
        stock_data = yf.download(ticker, start=dt.datetime.today() - dt.timedelta(days=365), end=dt.datetime.today())
        mpf.plot(stock_data, type='candle', mav=(10, 20, 30), volume=True, show_nontrading=True, title=f"Yearly Candlestick Chart for {ticker}")





# Create new portfolio object
my_portfolio = Portfolio()

# Add some positions
my_portfolio.add_stock('AAPL', 10)
my_portfolio.add_stock('GOOG', 5)
my_portfolio.add_stock('TSLA', 3)

# Display portfolio
#my_portfolio.display()
# Display pie chart
#my_portfolio.plot_pie_chart()
# Display chart
#my_portfolio.yearly_candlestick_chart('AAPL')






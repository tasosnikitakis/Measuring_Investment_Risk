import yfinance as yf
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates


class Portfolio:
    def __init__(self, tickers, num_stocks):
        self.tickers = tickers
        self.num_stocks = num_stocks
        self.prices = self._fetch_prices()
        self.actions = []

    def _fetch_prices(self):
        prices = []
        for ticker in self.tickers:
            ticker_data = yf.Ticker(ticker)
            ticker_price = ticker_data.history(period="1d")["Close"][0]
            prices.append(ticker_price)
        return np.array(prices)

    def get_weights(self, total_stocks):
        # Calculate the weights
        weights = self.prices * np.array(self.num_stocks) / sum(self.prices * self.num_stocks)

        # Scale the weights to add up to 1
        weights /= sum(weights)

        # Scale the weights to the total number of stocks in the portfolio
        weights *= total_stocks

        return weights

    def add_stocks(self, tickers, num_stocks):
        # Add stocks to the portfolio
        for ticker, num in zip(tickers, num_stocks):
            if ticker in self.tickers:
                idx = self.tickers.index(ticker)
                self.num_stocks[idx] += num
            else:
                self.tickers.append(ticker)
                self.num_stocks.append(num)
                ticker_data = yf.Ticker(ticker)
                ticker_price = ticker_data.history(period="1mo")["Close"][0]
                self.prices = np.append(self.prices, ticker_price)

        # Add the action to the list of actions
        action = {'type': 'add', 'tickers': tickers, 'num_stocks': num_stocks}
        self.actions.append(action)

    def sell_stocks(self, tickers, num_stocks):
        # Sell stocks from the portfolio
        for ticker, num in zip(tickers, num_stocks):
            idx = self.tickers.index(ticker)
            if num > self.num_stocks[idx]:
                raise ValueError("Trying to sell more stocks than available in the portfolio")
            self.num_stocks[idx] -= num

        # Add the action to the list of actions
        action = {'type': 'sell', 'tickers': tickers, 'num_stocks': num_stocks}
        self.actions.append(action)


class StockGraph:
    def __init__(self, ticker):
        self.ticker = ticker
        self.data = self._fetch_data()

    def _fetch_data(self):
        return yf.Ticker(self.ticker).history(period="max")

    def plot_candlestick(self):
        # Extract the necessary data for the candlestick chart
        ohlc = self.data[["Open", "High", "Low", "Close"]]
        ohlc.index = mdates.date2num(ohlc.index)
        ohlc = ohlc.astype(float)

        # Create the figure and axis objects
        fig, ax = plt.subplots()
        fig.subplots_adjust(bottom=0.2)
        ax.xaxis_date()

        # Plot the candlestick chart
        candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='g', colordown='r')

        # Format the x-axis ticks
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.xticks(rotation=45)

        # Set the title and labels
        plt.title(self.ticker)
        plt.xlabel("Date")
        plt.ylabel("Price")

        # Show the plot
        plt.show()

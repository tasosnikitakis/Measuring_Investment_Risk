# Import the necessary libraries
import yfinance as yf
from Classes import Portfolio
from Classes import StockGraph

# Define the portfolio object
portfolio = Portfolio("AAPL", 10)

# Add stocks to the portfolio
portfolio.add_stock("AAPL", 10)
portfolio.add_stock("GOOG", 5)

# Fetch the latest stock prices
portfolio.fetch_latest_prices()

# Print the portfolio weights
print(portfolio.weights())

# Plot the candlestick chart for AAPL
aapl_graph = StockGraph("AAPL")
aapl_graph.plot_candlestick()

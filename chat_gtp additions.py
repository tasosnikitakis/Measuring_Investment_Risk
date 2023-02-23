def calculate_portfolio_weights(tickers, num_stocks, total_stocks):
    # Fetch the latest price for each ticker
    prices = []
    for ticker in tickers:
        ticker_data = yf.Ticker(ticker)
        ticker_price = ticker_data.history(period="1d")["Close"][0]
        prices.append(ticker_price)

    # Calculate the weights
    weights = np.array(prices) * np.array(num_stocks) / sum(prices * num_stocks)

    # Scale the weights to add up to 1
    weights /= sum(weights)

    # Scale the weights to the total number of stocks in the portfolio
    weights *= total_stocks

    return weights


# Example usage:
tickers = ["AAPL", "MSFT", "AMZN"]
num_stocks = [10, 20, 30]
total_stocks = 100
weights = calculate_portfolio_weights(tickers, num_stocks, total_stocks)
print(weights)


#packages install
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
yf.pdr_override()
import matplotlib.pyplot as plt


#getting data
tickers = ["AMD", "NVDA"]

sec_data = pd.DataFrame()
for t in tickers:
    sec_data[t] = pdr.get_data_yahoo(t, start = "2018-1-1")["Adj Close"]

print(sec_data.tail())

# calculating returns
sec_returns = np.log(sec_data / sec_data.shift(1))
print(sec_returns.tail())

# AMD mean and standard deviation calculation
mean_AMD = sec_returns["AMD"].mean()
# mean calculation by numpy
print(mean_AMD)
# mean annualization
mean_AMD_annualized = sec_returns["AMD"].mean() * 250
print(mean_AMD_annualized)
# standard deviation calculation by numpy
standard_deviation_AMD = sec_returns["AMD"].std()
print(standard_deviation_AMD)
# standard deviation annualized
standard_deviation_AMD_annualized = sec_returns["AMD"].std() * 250 ** 0.5
print(standard_deviation_AMD_annualized)

# comparisons
mean_comparisons = sec_returns[["AMD", "NVDA"]].mean() * 250
print(mean_comparisons)
std_comparisons = sec_returns[["AMD", "NVDA"]].std() * 250 ** 0.5
print(std_comparisons)

# covariance and correlation
# variance calculation using the numpy var function
AMD_var = sec_returns["AMD"].var()
print(f"AMD Variance: {AMD_var}")
# annu8alized variance calculation
AMD_var_annualized = sec_returns["AMD"].var() * 250
print(f"AMD annualized variance: {AMD_var_annualized}")

# covariance calculation
cov_returns_matrix = sec_returns.cov()
print(cov_returns_matrix)
# Covariance matrix constructed using the cov() pandas dataframe method
# the pandas.dataframe.cov() calculates the covariance of a pair of columns

# Annualized covariance calculation
cov_returns_matrix_annualized = sec_returns.cov() * 250
print(cov_returns_matrix_annualized)

# correlation matrix
corr_matrix = sec_returns.corr()
print(corr_matrix)



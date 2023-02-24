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
    sec_data[t] = pdr.get_data_yahoo(t, start = "2015-1-1")["Adj Close"]

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

# NVDA mean and standard deviation calculation
mean_NVDA = sec_returns["NVDA"].mean()
# mean calculation by numpy
print(mean_NVDA)
# mean annualization
mean_NVDA_annualized = sec_returns["NVDA"].mean() * 250
print(mean_NVDA_annualized)
# standard deviation calculation by numpy
standard_deviation_NVDA = sec_returns["NVDA"].std()
print(standard_deviation_NVDA)
# standard deviation annualized
standard_deviation_NVDA_annualized = sec_returns["NVDA"].std() * 250 ** 0.5
print(standard_deviation_NVDA_annualized)


# comparisons
mean_comparisons = sec_returns[["AMD", "NVDA"]].mean() * 250
print(mean_comparisons)
std_comparisons = sec_returns[["AMD", "NVDA"]].std() * 250 ** 0.5
print(std_comparisons)

# covariance and correlation
# variance calculation using the numpy var function
AMD_var = sec_returns["AMD"].var()
print(f"AMD Variance: {AMD_var}")
# annualized variance calculation
AMD_var_annualized = sec_returns["AMD"].var() * 250
print(f"AMD annualized variance: {AMD_var_annualized}")
# variance calculation using the numpy var function
NVDA_var = sec_returns["NVDA"].var()
print(f"NVDA Variance: {NVDA_var}")
# annualized variance calculation
NVDA_var_annualized = sec_returns["NVDA"].var() * 250
print(f"NVDA annualized variance: {NVDA_var_annualized}")


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

#Calculating portfolio risk
weights_array = np.array([0.5, 0.5])
# portfolio variance calculation
portfolio_var = np.dot(weights_array.T, np.dot(sec_returns.cov() * 250, weights_array))
print(f"Portfolio variance is: {round(portfolio_var * 100, 2)}%")
# portfolio volatility calculation
portfolio_vol = np.dot(weights_array.T, np.dot(sec_returns.cov() * 250, weights_array)) ** 0.5
portfolio_vol_rounded_percentaga = round(portfolio_vol *100, 2)
print(f"Portfolio volatility is: {portfolio_vol_rounded_percentaga}%")

#Calculating diversifiable and non diversifiable risk
# Diversifiable risk calculation
#Diversifiable risk = Portfolio Variance - Weighted Annual Variances of each stock
weights = np.array([0.5, 0.5])
dr = portfolio_var - (weights[0] ** 2 * AMD_var_annualized) - (weights[1] ** 2 * NVDA_var_annualized)
print(f"Diversifiable portfolio risk is {str(round(dr*100, 3))}%")
#Non Diversifiable risk calculation
#Non Diversifiable risk = Portfolio Variance - Diversifiable risk
ndr = portfolio_var - dr
print(f"Non diversifiable portfolio risk is {str(round(ndr*100, 3))}%")
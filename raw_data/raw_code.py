import pandas as pd
import numpy as np
import streamlit as st
import scipy as sc
import statistics
from scipy import stats
from scipy.stats import gmean
from scipy.stats import hmean
import openpyxl

file_path = "raw_data.xlsx"

cars = pd.read_excel(file_path, header=None)

cars

df = cars.describe()
df

count = df.iloc[0]
mean = df.iloc[1]
std = df.iloc[2]
min = df.iloc[3]
firstpercentile = df.iloc[4]
secondpercentile = df.iloc[5]
thirdpercentile = df.iloc[6]
max = df.iloc[7]

float(count[0])

float(mean[0])

float(std[0])

float(min[0])

float(firstpercentile[0])

float(secondpercentile[0])

float(thirdpercentile[0])

variance = std**2
float(variance[0])

sum = np.sum(cars, axis=0)
float(sum[0])

mode = stats.mode(cars, axis=None, keepdims=False)
float(mode[0])

median = np.median(cars)
float(median)

standard_error = std / np.sqrt(count)
float(standard_error[0])

kurtosis = stats.kurtosis(cars, bias=False)
float(kurtosis[0])

skewness = stats.skew(cars, bias=False)
float(skewness[0])

range = np.ptp(cars)
float(range)

geometric_mean = gmean(cars)
float(geometric_mean[0])

harmonic_mean = hmean(cars)
float(harmonic_mean[0])

median_abs_deviation = stats.median_abs_deviation(cars)
float(median_abs_deviation[0])

iqr = stats.iqr(cars)
float(iqr)

cv = stats.variation(cars) *100
str(round(cv[0],2)) + "%"


def ave_dev(series):
    mean = series.mean()
    abs_devs = (series - mean).abs()
    return abs_devs.mean()

add = ave_dev(cars)
float(add[0])

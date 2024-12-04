import pandas as pd
import numpy as np

from pandas.tseries.offsets import YearEnd
from pandas.tseries.holiday import USFederalHolidayCalendar

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import ticker

import seaborn as sns

import scipy.stats as stats

from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm

from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

import streamlit as st

import warnings
warnings.filterwarnings('ignore')

def mape(y_true, y_pred, round=None) -> float:
    ''' Calculates the mean absolute percentage error.
    
    Parameters
    ----------
    y_true : array-like
        Ground truth (correct) target values.
    y_pred : array-like
        Estimated target values.
    round : int, optional
        Number of decimal places to round the result. The default is None.
    
    Returns
    -------
    float
        Mean absolute percentage error.
    '''

    if round is not None:
        return np.round(np.mean(np.abs((y_true - y_pred) / y_true)) * 100, round)
    
    else:
        return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


## ----------------------------------------- ##
##                 Streamlit                 ##
## ----------------------------------------- ##

def insert_image(image_path, caption, source=None, width=600) -> None:
    '''
    Insert image in the streamlit app.
    
    Parameters:
    image_path: str, path to the image.
    caption: str, caption of the image.
    source: str, source of the image.
    width: int, width of the image. Default is 600.
    
    Returns:
    None
    '''

    st.image(image_path, width=width)
    # legenda
    if source is None:
        st.markdown(f'<p style=font-size: 12px">{caption}</p>', unsafe_allow_html=True)
    else:
        st.markdown(f'<p style=font-size: 12px">{caption} | <a href="{source}" target="_blank">[Link]</a></p>', unsafe_allow_html=True)
    

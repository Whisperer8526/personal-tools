from scipy import signal
import statsmodels.api as sm
from sklearn.cluster import DBSCAN

def get_lag(x, y):
    """
    Get lag between two timeseries. They need to have aligned datetime index
    """
    correlation = signal.correlate(x, y, mode="full")
    lags = signal.correlation_lags(x.size, y.size, mode="full")
    lag = lags[np.argmax(correlation)]
    return lag


def detrend_timeseries_data(data):
    """
    Detrends data in all columns and add detrended data as new columns with '_detrend' suffix.
    Requires datetime index.
    """

    for column in data.columns:
        result = sm.tsa.seasonal_decompose(data[column])
        detrend = data[column] - result.trend
        data[f'{column}_detrend'] = detrend

    return data.dropna()

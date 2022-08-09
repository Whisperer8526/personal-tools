from scipy import signal
import statsmodels.api as sm
from sklearn.cluster import DBSCAN

def get_lag(x, y):
    """Get lag between two timeseries. They need to have aligned datetime index"""

    correlation = signal.correlate(data["closing_price_detrend"], 
                               data["volume_detrend"], 
                               mode="full")

    lags = signal.correlation_lags(data["closing_price_detrend"].size, data["volume_detrend"].size, 
                                   mode="full")
    lag = lags[np.argmax(correlation)]
    return lag

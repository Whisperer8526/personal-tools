import seaborn as sns
import matplotlib.pyplot as plt
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


def plot_feature_and_outliers(data_and_mapped_outliers, feature_name, ax):
    """
    Plots outliers as red dots on time series lineplot.
    """
    # Get frame containing outliers only
    outlier_frame = data_and_mapped_outliers.loc[data_and_mapped_outliers[f"{feature_name}_detrend_outlier"]==True, f"{feature_name}_detrend"]
    # Line plot for relative humidity
    out = sns.lineplot(x=data_and_mapped_outliers.index, y=data_and_mapped_outliers[f"{feature_name}_detrend"], ax=ax) 
    # Adding outliers as red dots
    sns.scatterplot(x=outlier_frame.index, y=outlier_frame, color="red", ax=ax)
    # Title and lables
    out.set(xlabel='Date', ylabel=f'{feature_name}_detrend', title=f'{feature_name}')
    # Legend
    plt.legend(labels=[f'{feature_name}', 'Outlier'], ax=ax)

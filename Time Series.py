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
    

    
def plot_time_series(data_features, data_start_date, data_end_date):
    fig, ax = plt.subplots(figsize=(12, 7))
    ax = ax.xaxis_date()
    ax = plt.hlines(data_features, 
                    dates.date2num(data_start_date), 
                    dates.date2num(data_end_date),
                    linewidth=7)

    x_ticks = pd.date_range(start= data_start_date.min(), 
                           end= data_end_date.max(), freq='MS' )

    plt.xticks(ticks= x_ticks, 
               labels= [date.strftime("%m-%Y") for date in x_ticks],
               rotation=60)

    #plt.axvline(x=dt.datetime.now(), color='r', ls=':')
    
    return plt.show()

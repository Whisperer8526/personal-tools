def get_ranked_colors(data, color="RdBu_r"):
  '''
  Adjust color shade to feature value. It should be placed as value of 
  palette parameter

  Arguments:
    data : pandas DataFrame or Series
    color : (optional) Color paplette name
  Returns:
    Custom color palette
  '''
  import numpy as np
  import seaborn as sns

  pal = sns.color_palette(color, len(data.index))
  rank = data.argsort().argsort()

  return np.array(pal)[rank]


def get_multi_countplot(data, n_row=1, n_col=1, figsize=(20,20)):
  '''
  Draws countplot for every column in dataset
   
  Arguments:
    data : pandas DataFrame
    n_row : (optional) number of rows
    n_col : (optional) number of columns
    figsize : (optional) plot size in inches
  Returns:
    Plot containing subplots
  '''
  import seaborn as sns
  import matplotlib.pyplot as plt
  
  fig, axes = plt.subplots(n_row, n_col, figsize=figsize)
  idx = ((x,y) for x in range(n_row) for y in range(n_col))

  for column in data.columns:
    sns.countplot(x=column, data=data, ax=axes[next(idx)])

  return plt.show()


def draw_correlation_matrix_heatmap(data, size_width=10, size_height=10):

    corr_matrix = data.corr()
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

    fig, ax = plt.subplots(figsize=(size_width, size_height))
    
    return sns.heatmap(corr_matrix, 
                       annot=True, 
                       square=True, 
                       ax=ax, 
                       vmin=-1, 
                       vmax=1, 
                       cmap="RdBu_r", 
                       mask=mask)
  
  
def plot_event_duration(labels, start_dates, end_dates, linewidth=7, figsize=(15,7)):
    
    import datetime as dt
    import matplotlib.pyplot as plt
    import matplotlib.dates as dates
    
    fig, ax = plt.subplots(figsize=figsize)
    ax = ax.xaxis_date()
    ax = plt.hlines(labels, 
                    dates.date2num(start_dates), 
                    dates.date2num(end_dates),
                    linewidth=linewidth)

    x_ticks = pd.date_range(start= start_dates.min(), 
                           end= dt.datetime.now(), freq='MS' )

    plt.xticks(ticks= x_ticks, 
               labels= [date.strftime("%m-%Y") for date in x_ticks],
               rotation=60)

    #plt.axvline(x=dt.datetime.now(), color='r', ls=(':'))
    #plt.axvline(x=dt.datetime(2021,1,1).date(), color='gray', ls=':', linewidth=1)
    #plt.axvline(x=dt.datetime(2022,1,1).date(), color='gray', ls=':', linewidth=1)
    
    return plt.show()

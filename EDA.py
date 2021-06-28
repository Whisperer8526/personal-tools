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

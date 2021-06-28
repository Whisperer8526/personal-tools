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
  import pandas as pd
  import seaborn as sns

  pal = sns.color_palette(color, len(data.index))
  rank = data.argsort().argsort()

  return np.array(pal)[rank]

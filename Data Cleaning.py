def remove_outliers(data, contamination='auto'):
    from sklearn.ensemble import IsolationForest
    
    # Fitting algorythm to data and saving results in pd.Series type variable.
    initial_size = len(data)
    data_array = np.array(data)
    iso = IsolationForest(n_estimators=1000, contamination=contamination)
    preds = iso.fit_predict(data_array)
    outliers = pd.Series(preds, index=data.index)

    # Creating new "boolean" type column containing information if given value is an outlier

    data["outlier"] = outliers < 0

    data = data[data["outlier"]==False] # Removing outliers from dataset
    data = data.drop(columns=['outlier'])
    print(f'Removed {initial_size - len(data)} outliers')
    
    return data

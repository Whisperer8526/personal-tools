def highlight_row(data, index_value):
    series = [True if i[1] == index_value else False for i in data.index]
    series = pd.concat([pd.Series(series)] * data.shape[1], axis=1)
    result = pd.DataFrame(np.where(series, 'background-color:#F5F5F5', ''),
                     index=data.index, columns=data.columns)
    return result

def highlight_column(data, column_value):
    series = [True if column_value in i[1] else False for i in data.columns]
    series = pd.concat(data.shape[0] * [pd.Series(series)], axis=1).T
    result = pd.DataFrame(np.where(series, 'num_format: {:.2%}', ''),
                     index=data.index, columns=data.columns)
    return result

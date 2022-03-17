def z_test(df):
    global total_engaged, total_non_engaged, total_respondents, get_z_test
        
    def p_val_transform(val):
        if type(val) is not np.float64:
            return val
        else:
            if val < 0.05:
                return "<0.05"
            elif val < 0.15:
                return "<0.15"
            elif val > 0.15:
                return "N"
    

    vals = []
    for index, row in df[:-2].iterrows():
        if row[0] > 50 and row[1] > 50:
            non_eng_prop = row[0] / total_non_engaged
            eng_prop = row[1] / total_engaged
            row_sum = row[0] + row[1]
            prop = row_sum / total_respondents
            z_stat = (non_eng_prop - eng_prop) / sqrt(prop * (1 - prop) * (1/df.iloc[-2,0] + 1/df.iloc[-2,1]))
            p = 2 * (1 - norm.cdf(abs(z_stat)))
            vals.append(p)
        else:
            vals.append("N/A")

    for i in range(len(df[-2:])):
        vals.append('')
    df['stat'] = vals
    df['Stat sig'] = df['stat'].apply(lambda x: p_val_transform(x))
    df = df.drop(columns="stat")

    return(df)

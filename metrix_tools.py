def match_twitter_posts(links_file, export_file):

    links = pd.read_excel(links_file)
    links['post_id'] = links.iloc[:,0].apply(lambda x: x.split('/')[-1])

    export = pd.read_excel(export_file)
    export['post_id'] = export['Link to post'].apply(lambda x: x.split('/')[-1])

    matched_posts =  pd.merge(data, export, on='post_id')
    
    return matched_posts

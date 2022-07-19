def match_twitter_posts(links_file, export_file):

    links = pd.read_excel(links_file)
    links['post_id'] = links.iloc[:,0].apply(lambda x: x.split('/')[-1])

    export = pd.read_excel(export_file)
    export['post_id'] = export['Link to post'].apply(lambda x: x.split('/')[-1])

    matched_posts =  pd.merge(data, export, on='post_id')
    
    return matched_posts


def get_clean_url(link: str):
    fb_link_formats = ['facebook.com', 'fb.com']
    for item in fb_link_formats:
        if item in link:
            url = urlopen(link, context=certificate)
            page = BeautifulSoup(url.read(), 'lxml')
            #sleep(0.1)
            links = page.find_all('link', href=True)

            link_list = []
            for item in links:
                if 'www.facebook.com' in item['href']:
                    link_list.append(item['href'])
            if len(link_list) == 0:
                return link
            if 'login/web' in link_list[0]:
                return link
            else:
                return link_list[0]
        
        else:
            return link

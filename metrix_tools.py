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
        
 
def map_post_id(link: str):
    try:
        if 'twitter.com' in link:
            return int(link.split('/')[-1].split('?')[0])
        if 'tiktok.com' in link:
            return int(link.split('/')[-1])
        elif 'facebook.com' in link:
            try:
                post_id = int(link.split('/')[-1])
            except:
                if '?dco_ad_id' in link:
                    return int(link.split('?dco_ad_id')[0].split('/')[-1])
                else:
                    try:
                        post_id = int(link.split('/')[-2])
                    except:
                        post_id = 0

            return post_id
        
        elif 'instagram.com' in link:
            post_id = link.split('/')[-1]
            if '#advertiser' in post_id:
                return link.split('/')[-2]
            elif len(post_id) != 0 and 'copy_link' not in post_id:
                return post_id
            else:
                return link.split('/')[-2]

        elif 'youtube.com' in link:
            return link.split('?v=')[-1]
        else:
            return np.nan
    except:
        return np.nan

    
def get_fb_page_id(link):
    url = urlopen(link, context=certificate)
    page = BeautifulSoup(url.read(), 'lxml')
    page_id_pattern = re.compile(r"PageID\(\"(.*?)-")
    page_id = re.search(page_id_pattern, str(page))
    
    if page_id == None:
        page_id_pattern = re.compile(r"\"pageLoadEventId\":\"(.*?)\"")
        page_id = re.search(page_id_pattern, str(page))
    
    return int(page_id.group(1))


def get_ad_id(link):
    ad_id = np.nan
    if 'facebook.com' in link:
        if '?dco_ad_id=' in link:
            try:
                ad_id = int(link.split('?dco_ad_id=')[-1])
            except:
                ad_id = int(link.split('?dco_ad_id=')[-1].split('&dco_ad_token')[0])
    
    return ad_id

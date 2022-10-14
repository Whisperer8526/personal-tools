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
            return str(link.split('/')[-1].split('?')[0])
        elif 'tiktok.com' in link:
            try:
                return str(int(link.split('/')[-1]))
            except:
                return str(link.split('/')[-1].split('?')[0])
        elif 'facebook.com' in link:
            try:
                post_id = int(link.split('/')[-1])
            except:
                if '?dco_ad_id' in link:
                    return str(int(link.split('?dco_ad_id')[0].split('/')[-1]))
                else:
                    try:
                        post_id = int(link.split('/')[-2])
                    except:
                        try:
                            post_id = int(link.split('?s=')[-2].split('/')[-1])
                        except:
                            post_id = 0

            return str(post_id).rstrip('.0')
        
        elif 'fb.watch' in link:
            url = urlopen(link, context=certificate)
            page = BeautifulSoup(url.read(), 'lxml')
            try:
                pattern = re.compile(r'\"video_id\":\"(.*?)\"')
                post_id = re.search(pattern, str(page)).group(1)
            except AttributeError:
                pattern = re.compile(r'\"v\":\"(.*?)\"')
                post_id = re.search(pattern, str(page)).group(1)
            
            return str(post_id).rstrip('.0')
        
        
        elif 'instagram.com' in link and GET_IG_POST_IDS:
            shortcode = map_ig_shortcode(link)
            url = urlopen(f'https://www.instagram.com/p/{shortcode}/', context=certificate)
            page = BeautifulSoup(url.read(), 'lxml')
            pattern = re.compile(r"\"media_id\":\"(.*?)\"")
            post_id = int(re.search(pattern, str(page)).group(1))
            
            return post_id

        elif 'youtube.com' in link:
            if 'shorts' in link:
                return link.split('/')[-1]
            else:
                return link.split('?v=')[-1].split('&v=')[-1]
        
        elif 'youtu.be' in link:
            return link.split('/')[-1].split('?t=')[0]
        
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

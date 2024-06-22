import bs4, requests as re


def fetchSource(url=''):
    ''' Fetch the given url, returns the page text'''
    resp = None
    if 'http' in url or 'https' in url:
        resp = re.get(url)
    else:
        resp = re.get('https://' + url)
    if resp.status_code == 200:
        return resp.text
    else:
        return None

def sourceLinkMiner(content=''):
    '''Extract highlights from link tags, returns a list of (text, urls)'''
    highlights = []
    # get all links, with their text word & href
    soup = bs4.BeautifulSoup(content , 'html.parser')
    links = soup.find_all('a')

    print("found: ", len(links))
    # for each link get the text & href url
    for _, link in enumerate(links):
        if link.string == None:
            if link.get('href') != None:
                url = link['href'].strip()
                if len(url) > 3:
                    hgl = (None, url)
                    highlights.append(hgl)
        else:
            text = link.string.strip()
            hgl = (text, link['href'].strip())
            highlights.append(hgl)
    return highlights

def sourceHsMiner(content=''):
    pass

def sourceDivsMiner(content=''):
    pass

def sourceParagsMiner(content=''):
    pass

def sourceSpanMiner(content=''):
    pass




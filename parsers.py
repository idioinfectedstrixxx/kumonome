from bs4 import BeautifulSoup
import logwriting
import re
import requests
from threading import Thread
import urllib
from urllib.request import urlopen
#Video parser classes// TODO: add some hostings excepting YouTube
class Yt_Parser:
    def __init__(self, mode, max_views):
        self.mode = mode
        self.max_views = max_views

    def raw_search(self, query):
        if self.mode == "vid":
            url = f"https://www.youtube.com/results?search_query={query}&sp=EgIQAQ%253D%253D"
        elif self.mode == "chan":
            url = f"https://www.youtube.com/results?search_query={query}&sp=EgIQAg%253D%253D"
        elif self.mode == "plists":
            url = f"https://www.youtube.com/results?search_query={query}&sp=EgIQAw%253D%253D"
        rpage = requests.get(url)
        soup = BeautifulSoup(rpage.text, "html.parser")
        s = soup.find_all("script")
        if self.mode == "vid":
            key = '"videoRenderer":'
            m = re.findall(key + r'(.*?)\{"playlistId":"WL","actions":\[\{"action":"', str(s))
        elif self.mode == "chan":
            key = '{"channelRenderer":{'
            m = re.findall(r'\{"channelRenderer":\{(.*?)}]},"shortBylineText"', str(s))
        elif self.mode == "plists":
            m = re.findall('\{"playlistRenderer"(.*?)"webPageType":"WEB_PAGE_TYPE_CHANNEL"', str(s))
        return m

    def get_params_vid(self, text):
        params = []
        # video id
        id_key = '"videoId":"'
        vidid = re.search(id_key + r'([^*]{11})', text)
        string_id = vidid[0]
        url = "https://www.youtube.com/watch?v=" + string_id[11:]
        params.append(url)
        # view_chk
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        views = re.findall(r'"viewCount":"(.*?)"', str(soup))
        vcnt = views[0]
        if int(vcnt) > self.max_views:
            pass
            return None
        else:
            params.append(int(vcnt))
            date_raw = re.findall(r'itemprop="datePublished"/><meta content="(.*?)" itemprop="uploadDate"', str(soup))
            dt = date_raw[0]
            params.append(dt.replace('T', ' at '))
            # video title
            t_text = re.findall(r'"title":\{"runs":\[\{"text":"(.*?)"}],"accessibility":', text)
            title = t_text[0]
            params.append(title)
            # author
            p_text = re.findall(r'"webCommandMetadata":\{"url":"(.*?)","webPageType"', text)
            author = f"https://www.youtube.com{p_text[0]}"
            params.append(author)
            #preview
            try:
                thumbn = re.findall(r'"thumbnail":\{"thumbnails":\[\{"url":"(.*?)\?', text)
                thumblink = thumbn[0]
            except:
                thumblink = "<ThumbnailError>"
            params.append(thumblink)
            #duration
            d_txt = re.findall(r'}},"simpleText":"(.*?)"},"viewCountText":', text)
            dur = d_txt[0]
            params.append(dur)
            return params

    def get_params_chan(self, text):
        params = []
        #get name
        ttl = re.findall(r',"title":\{"simpleText":"(.*?)"},"navigationEndpoint"', text)
        chan_title = ttl[0]
        params.append(chan_title)
        # channel id
        id_key = '"channelId":"'
        chid = re.search(id_key + r'([^*]{24})', text)
        string_id = chid[0]
        url = "https://www.youtube.com/channel/" + string_id[13:37]
        params.append(url)
        # subscribers count
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        subs = re.findall(r'"videoCountText":\{"accessibility":\{"accessibilityData":\{"label":"(.*?)"}}', str(soup))
        try:
            scnt_text = subs[0]
            params.append(scnt_text)
        except:
            pass
        #trying to get pfp
        try:
            thumb_txt = re.findall(r'"thumbnail":\{"thumbnails":\[\{"url":"//(.*?)","width"',text)
            thumblink = f'http://{thumb_txt[-1]}'
        except:
            thumblink = "<ThumbnailError>"
        params.append(thumblink)
        return params

    def get_params_pl(self, text):
        params = []
        #get id
        idstext = re.findall(r'"playlistId":"([^*]{34})', text)
        params.append(idstext[0])
        #get title
        ttl = re.findall(r'"title":\{"simpleText":"(.*?)"},', text)
        params.append(ttl[0])
        #count of videos
        vc = re.findall(r'"videoCount":"(.*?)"',text)
        params.append(int(vc[0]))
        #authors channel
        id = re.findall(r'\{"webCommandMetadata":\{"url":"/@(.*?)",', text)
        params.append(f'https://youtube.com/{id[0]}')
        return params



            

    def search(self, query):
        m = self.raw_search(query)
        for i in range(len(m)):
            l = str(m[i])
            if self.mode == 'vid':
                params = self.get_params_vid(l)
            elif self.mode == 'chan':
                params = self.get_params_chan(l)
            elif self.mode == 'plists':
                params = self.get_params_pl(l)
            if params is None:
                pass
            else:
                with open('logs.txt', 'a+', encoding='utf-8') as logs:
                    try:
                        if self.mode == 'vid':
                            logs.write(f'--{params[3]}--\nlink: {params[0]}\nuploaded by: {params[4]}\nupload date: {params[2]}\n{params[1]} views\n\n\n')
                            print(f'--{params[3]}--\nlink: {params[0]}\nuploaded by: {params[4]}\nupload date: {params[2]}\n{params[1]} views\n\n\n')
                            try:
                                urllib.request.urlretrieve(params[5], f"{params[3]}_thumb.jpg")
                            except:
                                pass
                        elif self.mode == 'chan':
                            logs.write(f'--{params[0]}--\nlink: {params[1]}\n{params[2]} subscribers\n\n')
                            print(f'--{params[0]}--\nlink: {params[1]}\n{params[2]} subscribers\n\n')
                            try:
                                urllib.request.urlretrieve(params[-1], f"{params[0]}_pfp.jpg")
                            except:
                                pass
                        elif self.mode == 'plists':
                            logs.write(f'--{params[1]}--\nlink: https://www.youtube.com/playlist?list={params[0]}\n{params[2]} videos\nAuthor: https://www.youtube.com/@{params[3]}\n\n')
                            print(f'--{params[1]}--\nlink: https://www.youtube.com/playlist?list={params[0]}\n{params[2]} videos\nAuthor: https://www.youtube.com/@{params[3]}\n\n')
                    except TypeError:
                        pass


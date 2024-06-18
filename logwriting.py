from bs4 import BeautifulSoup
from datetime import datetime
import os
import urllib
from urllib.request import urlopen

def add_pict(picurl, pict):
    urllib.request.urlretrieve(picurl, pict)
def make_logs_dir():
    folder_date = (str(datetime.now().date()))
    folder_name = f"kumonome_logs_{folder_date}"
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        pass
    return folder_name
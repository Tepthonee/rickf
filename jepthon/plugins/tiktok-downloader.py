# Copyright 2021 TerminalWarlord under the terms of the MIT
# license found at https://github.com/TerminalWarlord/TikTok-Downloader-Bot/blob/master/LICENSE
# Encoding = 'utf-8'
# Fork and Deploy, do not modify this repo and claim it yours
# For collaboration mail me at dev.jaybee@gmail.com

from telethon import filters
import shutil
import requests
import json
import os
import re
from bs4 import BeautifulSoup as bs
import time
from datetime import timedelta
import math
import base64
from progress_bar import progress, TimeFormatter, humanbytes
from jepthon import jmthon 
from ..Config import Config

@jmthon.ar_cmd((filters.regex("http://")|filters.regex("https://")) & (filters.regex('tiktok')|filters.regex('douyin')))
def tiktok_dl(message):
    a = app.send_message(chat_id=message.chat.id,
                         text='يجري تنزيل الملف للخادم..',
                         parse_mode='md')
    link = re.findall(r'\bhttps?://.*[(tiktok|douyin)]\S+', message.text)[0]
    link = link.split("?")[0]



    
    params = {
      "link": link
    }
    headers = {
      'x-rapidapi-host': "tiktok-info.p.rapidapi.com",
      'x-rapidapi-key': "f9d65af755msh3c8cac23b52a5eep108a33jsnbf7de971bb72"
    }
    
    ### Get your Free TikTok API from https://rapidapi.com/TerminalWarlord/api/tiktok-info/
    #Using the default one can stop working any moment 
    
    api = f"https://tiktok-info.p.rapidapi.com/dl/"
    r = requests.get(api, params=params, headers=headers).json()['videoLinks']['download']
    directory = str(round(time.time()))
    filename = str(int(time.time()))+'.mp4'
    size = int(requests.head(r).headers['Content-length'])
    total_size = "{:.2f}".format(int(size) / 1048576)
    try:
        os.mkdir(directory)
    except:
        pass
    with requests.get(r, timeout=(50, 10000), stream=True) as r:
        r.raise_for_status()
        with open(f'./{directory}/{filename}', 'wb') as f:
            chunk_size = 1048576
            dl = 0
            show = 1
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                dl = dl + chunk_size
                percent = round(dl * 100 / size)
                if percent > 100:
                    percent = 100
                if show == 1:
                    try:
                        a.edit(f'__**URL :**__ __{message.text}__\n'
                               f'__**Total Size :**__ __{total_size} MB__\n'
                               f'__**Downloaded :**__ __{percent}%__\n',
                               disable_web_preview=False)
                    except:
                        pass
                    if percent == 100:
                        show = 0

        a.edit(f' يجري التحميل للخادم..!\n'
               f' يجري الرفع للتلجرام⏳__')
        start = time.time()
        title = filename
        app.send_document(chat_id=message.chat.id,
                          document=f"./{directory}/{filename}",
                          caption=f"**File :** __{filename}__\n"
                          f"**Size :** __{total_size} MB__\n\n",
                          file_name=f"{directory}",
                          parse_mode='md',
                          progress=progress,
                          progress_args=(a, start, title))
        a.delete()
        try:
            shutil.rmtree(directory)
        except:
            pass

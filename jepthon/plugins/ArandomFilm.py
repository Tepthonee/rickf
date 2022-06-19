#Jepthon ©
#By Reda 
from imdb import Cinemagoer
import requests
from random import randint
from jepthon import jmthon
import asyncio
from ..core.managers import edit_delete, edit_or_reply
ia = Cinemagoer()

@jmthon.ar_cmd(pattern="فلم")
async def rfilm(event):
    for _ in range(100):
        movieID = f"{randint(1,9999999):07}"
        url = f'https://www.imdb.com/title/tt{movieID}'
        r = requests.get(url)
        if r.status_code != 200:
            continue

        movie = ia.get_movie(movieID)
        year = movie.get('year')
        rating = movie.get('rating', "لا يوجد")
        movien = movie.get('title')
        moviep = movie.get('cover url')
        movieimg = moviep or https://telegra.ph/file/15480332b663adae49205.jpg
        moviet = f"الاسم: {movien}\nالسنة: {year}\nالتقييم: {rating}"
        await jmthon.send_file(
                event.chat_id,
                str(movieimg),
                caption=moviet,
                )
        break

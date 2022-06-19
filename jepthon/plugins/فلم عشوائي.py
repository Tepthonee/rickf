from imdb import Cinemagoer
import requests
from random import randint
from jepthon import jmthon
import asyncio
from ..core.managers import edit_delete, edit_or_reply

ia = Cinemagoer()

@jmthon.ar_cmd(pattern="فلم")
async def rfilm(event):
    movieID = f'{randint(1,9999999):07}'
    url = f'https://www.imdb.com/title/tt{movieID}'
    r = requests.get(url)
    if r.status_code != 200:
        movie = ia.get_movie(movieID)
        votes = movie.get('votes', None)
        rating = movie.get('rating', None)
        await edit_or_reply(event, f"{movie}\n{votes}\n{rating}")

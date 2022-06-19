from imdb import Cinemagoer
import requests
from random import randint

ia = Cinemagoer()
@jmthon.ar_cmd(pattern="فلم")
async def rfilm(event)
    for _ in range(100):
        movieID = f'{randint(1,9999999):07}'
        url = f'https://www.imdb.com/title/tt{movieID}'
        r = requests.get(url)
        if r.status_code != 200:
            continue

        movie = ia.get_movie(movieID)
        print(movie)
        votes = movie.get('votes', None)
        print(votes)
        rating = movie.get('rating', None)
        print(rating)

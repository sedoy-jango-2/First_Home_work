import requests
import time

api_key = '2a186c2089eb4389fe6b60217c09a85f'
tmdb = 'https://api.themoviedb.org/3/'
max_n = 99999


def make_api_request(what, extra_parameters=None):
    extra_parameters = extra_parameters or {}
    url = tmdb + what
    payload = {
        'api_key': api_key,
        'language': 'ru'
    }
    payload.update(extra_parameters)
    movieUrl = requests.get(url, data=payload)
    if movieUrl.headers['X-RateLimit-Remaining'] <= '3':
        time.sleep(10)
    if movieUrl.status_code == 200:
        movieUrl = movieUrl.json()
        return movieUrl
    else:
        return 'error'

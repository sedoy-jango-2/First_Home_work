import urllib.request
import urllib.parse
import json

key = '2a186c2089eb4389fe6b60217c09a85f'

def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    try:
        print(urllib.request.__version__)
        print(urllib.request.get_header('X-RateLimit-Remaining', default=None))
        response = urllib.request.urlopen(url).read().decode('utf-8')
        return json.loads(response)
    except urllib.error.HTTPError:
        return 'False'



def make_tmdb_api_request(method, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': key,
        'language': 'ru',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)
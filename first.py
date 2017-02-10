import ppapi
import sys



a = ppapi.make_tmdb_api_request(method='/movie/1')
if a == 'False':
    print('Такого фильма не сущесвует')
    exit()
else:
    print('Бюджет фильма', a['title'], 'равен', a['budget'], '$')
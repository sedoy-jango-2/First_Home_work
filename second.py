import ppapi


if __name__ == '__main__':
    try:
        movieNomber1 = int(input('Введите номера фильма с которого скачать: '))
        movieNomber2 = int(input('Введите номера фильма по который скачать: '))
        if movieNomber1<0 or movieNomber2<0 or movieNomber1>ppapi.max_n or movieNomber2>ppapi.max_n:
            print('Неправильные аргументы')
            exit()
    except ValueError:
        print('Введённые данные не являются числом')
        exit()
    print('Cкачиваются фильмы от', movieNomber1,'до',movieNomber2,sep=' ',end='\n')
    file = open('movies.json','a',encoding='utf-8')
    file.write(str(min(movieNomber1, movieNomber2))+'\n')
    file.write(str(max(movieNomber1, movieNomber2))+'\n')
    for i in range(min(movieNomber1, movieNomber2),max(movieNomber1, movieNomber2)):
        movie = ppapi.make_api_request('movie/' + str(i))
        if movie == 'error':
            print('Фильм с номером', i, 'не скачался')
            file.write('Фильма с таким номером'+str(i)+' не существует')
        else:
            print('Скачивается фильм с номером', i)
            newMovie = ppapi.make_api_request('movie/' + str(i) + '/keywords')
            movie.update(newMovie)
            newMovie = ppapi.make_api_request('movie/' + str(i) + '/similar')
            movie.update(newMovie)
            newMovie = ppapi.make_api_request('movie/' + str(i) + '/lists')
            movie.update(newMovie)
            file.write('Фильм с номером' + str(i)+'\n')
            for key, value in movie.items():
                file.write('{}:{}\n'.format(key, value))


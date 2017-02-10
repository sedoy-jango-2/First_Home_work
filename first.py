import ppapi


if __name__ == '__main__':
    try:
        movieNomber = int(input('Введите номер фильма: '))
    except ValueError:
        print('Введённые данные не являются числом')
        exit()

    print('Используется ', movieNomber,' номер фильма',sep='',end='\n')
    movieDict = ppapi.make_api_request('movie/' + str(movieNomber))
    if movieDict != 'error':
        print('''Бюджет фильма - "''', movieDict['title'], '''" составил ''', movieDict['budget'], ' долларов', sep='', end='')
    else:
        print('Фильма с таким номером не существует на даннном сайте')

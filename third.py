import os

preference = input('Введите ключевое слово\n')

try:
    file = open('movies.json', encoding='utf-8')
except IOError as e:
    print('Не удалось открыть файл')
else:
    with file:
        file.seek(0)
        if os.stat('movies.json').st_size != 0:
            flag = False
            for line in file.readlines():
                if line.find('title') == 0 and line.find(preference) > 0:
                    print(line[line.find(':') + 1:])
                    flag = True
            if not flag:
                print('Фильмов содержащих данное слово не существует')
        else:
            print('Файл пуст')
        file.close()

import os
import help_for_forth

preference = input('Введите фильм который Вам нравится\n')

try:
    file = open('movies.json', encoding='utf-8')
except IOError as e:
    print('Не удалось открыть файл с фильмами')
else:
    with file:
        file.seek(0)
        if os.stat('movies.json').st_size == 0:
            print('Файл пуст')
        else:
            flag = False
            lineMass = file.readlines()
            file.seek(0)
            for i, line in enumerate(file):
                if line.find('title') != -1 and (preference + '\n') == line[line.find(':') + 1:]:
                    adult = lineMass[i - 21][lineMass[i - 21].find(':') + 1:]
                    genresArray = help_for_forth.make_string_array(lineMass[i - 17], 'name', '}')
                    keywordsArray = help_for_forth.make_string_array(lineMass[i + 4], 'name', '}')
                    flag = True
            if not flag:
                print('Такого фильма нет в базе данных')
            else:
                print('Возможно, эти фильмы Вам понравятся')
                file.seek(0)
                for i, line in enumerate(file):
                    flag1 = False
                    flag2 = False
                    if line.find('adult') != -1 and adult == line[line.find(':') + 1:]:
                        newKeywordsArray = help_for_forth.make_string_array(lineMass[i + 25], 'name', '}')
                        newGenresArray = help_for_forth.make_string_array(lineMass[i + 4], 'name', '}')
                        flag1 = help_for_forth.comparison_in_arrayes(newKeywordsArray, keywordsArray)
                        flag2 = help_for_forth.comparison_in_arrayes(newGenresArray, genresArray)
                        if (flag1 or flag2) is True:
                            print(lineMass[i + 21][lineMass[i + 21].find(':') + 1:])
                            flag = True
                if not flag:
                    print('К сожалению, мы не нашли для Вас подходящего фильма в имеющейся базе')
        file.close()

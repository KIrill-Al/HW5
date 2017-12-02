"""https://pokeapi.co/ - ПОКЕМОНЫ!!!
Тут собрана вся информация о покемонах. Необходимо получить номер покемона и выдать краткую информацию о нем."""


import urllib.request
import urllib.error
import json


def get_int(num):
    if num.isdigit():
        return int(num)
    else:
        return get_int(input('Значение введено некорректно. Введите целое число больше нуля.'))


def get_pokemon_info(number):
    if (802 >= number >= 1):  # в базе всего 802 покемона
        url = 'http://pokeapi.co/api/v2/pokemon/' + str(number)
        rec = urllib.request.Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            res = urllib.request.urlopen(rec)
        except urllib.error.URLError:
            print('Не удалось связаться с сервером. Проверьте подключение к интернету.')
        else:
            pokemon = json.loads(res.read())
            result = '{}\t{}\t{}\t{}\n'.format('Номер'.ljust(15, ' '),
                                               'Имя'.ljust(15, ' '),
                                               'Рост'.ljust(15, ' '),
                                               'Масса'.ljust(15, ' '))
            result += '{}\t{}\t{}\t{}'.format(str(number).ljust(15, ' '),
                                              pokemon['name'].ljust(15, ' '),
                                              (str(pokemon['height'] / 10) + ' м').ljust(15, ' '),
                                              (str(pokemon['weight'] / 10) + ' кг').ljust(15, ' '))
            print(result)
    else:
        print('Покемона с таким номером в нашей базе нет!')


if __name__ == '__main__':
    get_pokemon_info(get_int(input('Введите номер покемона ')))
'''http://www.recipepuppy.com/about/api/ - это сервис для получения рецептов.
Задача простая: передаем список продуктов, получаем рецепты для этого списка продуктов '''
import urllib.request
import urllib.error
import json


def get_recipes(*ingredients):
    url = 'http://www.recipepuppy.com/api/?i='
    ingreds = ','.join(ingredients)
    try:
        res = urllib.request.urlopen(url + ingreds)
    except urllib.error.URLError:
        print('Не удалось связаться с сервером. Проверьте подключение к интернету.')
    else:
        recipies = json.loads(res.read())
        for recipe in recipies['results']:
            print('Рецепт: {}\nСсылка на рецепт: {}\n'.format(recipe['title'], recipe['href']))


if __name__ == '__main__':
    get_recipes('avocado', 'shrimp')
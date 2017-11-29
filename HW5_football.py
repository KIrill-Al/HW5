'''https://api.football-data.org/ - это сервис о футболе. Предоставить информацию о ТОП-5 популярных чемпионатах.
Вывести по каждому чемпионату первые пять команд с наибольшим числом забитых голов.'''
# ТОП 5 лиг взят с сайта http://misto.news/life_hack/top-10-futbolnyh-lig-mira-33864.html
import urllib.request
import urllib.error
import json


def get_top5_leagues_info():
    url = 'http://api.football-data.org/v1/competitions/'
    leagues = [['Английская премьер лига', 445],
               ['Ла лига', 455],
               ['Бундеслига', 452],
               ['Серия А', 456],
               ['Французская лига 1', 451]]
    team_name = 'teamName'
    points = 'points'
    goals = 'goals'
    for name_leag, code_leag in leagues:  # вывод топ 5 команд каждой лиги
        try:
            res = urllib.request.urlopen('{}/{}/leagueTable'.format(url, code_leag))
        except urllib.error.URLError:
            print('Не удалось связаться с сервером. Проверьте подключение к интернету.')
        else:
            print('\n\n{}\n'.format(name_leag))
            obj = json.loads(res.read())
            teams = list([team[team_name], team[points], team[goals]] for team in obj['standing'])
            teams.sort(key=lambda team: team[2], reverse=True)  # сортировка по голам
            maxlen = max([len(x[0]) for x in teams[:5]])  # макс длина строки для ровного вывода
            print('{}\t{}\t{}'.format('Команда'.ljust(maxlen, ' '), 'Очки', 'Голы'))
            for t_name, t_points, t_goals in teams[:5]:
                print('{}\t{}\t{}'.format(t_name.ljust(maxlen, ' '),
                                          str(t_points).ljust(4, ' '),
                                          str(t_goals).ljust(4, ' ')))


if __name__ == '__main__':
    get_top5_leagues_info()
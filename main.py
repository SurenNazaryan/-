import requests


def get_weather(point):
    params = {
       "q": "",
       "T": "",
       "n": "",
       "mM": "",
       "lang": "ru"
    }
    url = 'https://wttr.in/'
    point_url = f'{url}{point}'
    response = requests.get(point_url, params=params)
    response.raise_for_status()
    print(response.text)


get_weather('Лондон')
get_weather('SVO')
get_weather('Череповец')

import requests


def get_weather(point):
    params = {
       "q": "",
       "T": "",
       "n": "",
       "M": "",
       "lang": "ru"
    }
    url = f'https://wttr.in/{point}'
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


def print_weather():
    points = ['Лондон', 'SVO', 'Череповец']
    for point in points:
        print(get_weather(point))


if __name__ == '__main__':
    print_weather()


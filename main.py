import requests


url_template = 'https://wttr.in/{}?{}&lang={}'
url1 = url_template.format('Лондон', 'qTn', 'ru')
response1 = requests.get(url1)
response1.raise_for_status()
print(response1.text)
url2 = url_template.format('SVO', 'qTn', 'ru')
response2 = requests.get(url2)
response2.raise_for_status()
print(response2.text)
url3 = url_template.format('Череповец', 'qTnmM', 'ru')
response3 = requests.get(url3)
response3.raise_for_status()
print(response3.text)

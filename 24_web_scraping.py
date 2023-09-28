import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/weather/3633009'

selector_temp_max = '#daylink-1 > div.wr-day__body > div.wr-day__details-container > div > div.wr-day__temperature > div > div.wr-day-temperature__high > span.wr-day-temperature__high-value > span > span.wr-value--temperature--c'
selector_temp_min = '#daylink-1 > div.wr-day__body > div.wr-day__details-container > div > div.wr-day__temperature > div > div.wr-day-temperature__low > span.wr-day-temperature__low-value > span > span.wr-value--temperature--c'
response = requests.get(url)

#print(response)  --> <Response [200]>

if response.status_code == 200:
    codigo_fuente = response.text
    response.close()     #cerramos conexion 

    soup = BeautifulSoup(codigo_fuente)

    titulo = soup.find('title')
    print(titulo.text)     # sin el atributo text: <title>Maracaibo - BBC Weather</title>

    temperatura_max = soup.select_one(selector_temp_max).text
    print(f'{temperatura_max = }')

    temperatura_min = soup.select_one(selector_temp_min).text
    print(f'{temperatura_min = }')

#buscarlos por su identificador class

    temperaturas = soup.find_all('span','wr-value--temperature--c')
    temperatura_maxima = temperaturas[1].text
    temperatura_minima = temperaturas[2].text
    print(f'{temperatura_maxima = }')
    print(f'{temperatura_minima = }')

else:
    print("falló conexion")



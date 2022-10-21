import requests
import os

response = requests.get(
    'https://data.stadt-zuerich.ch/dataset/ted_taz_verkehrszaehlungen_werte_fussgaenger_velo/download/2022_verkehrszaehlungen_werte_fussgaenger_velo.csv')

if not os.path.exists('data.csv'):
    with open('data.csv', mode='wb') as f:
        f.write(response.content)

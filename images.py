
import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

url = "http://books.toscrape.com/"  # URL de base de la page
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
images = soup.find_all('img')

for image in images:
    image_url = url + image['src']  # Construire l'URL complète
    image_data = requests.get(image_url).content
    with open(image_url.split('/')[-1], 'wb') as f:
        f.write(image_data)
import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

# URL de la page d'accueil
url = "http://books.toscrape.com/"

# Envoyer une requête HTTP GET à l'URL
response = requests.get(url)

# Vérifier si la requête a réussi (code de statut 200)
if response.status_code == 200:
    # Parser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Trouver  tous les liens vers les catégories
    category_links = [link['href'] for link in soup.find_all('a') if 'category' in link.get('href') and link.get('href').endswith('.html')]

    # Itérer sur chaque lien de catégorie
    for category_link in category_links:
        category_url = url + category_link
        response = requests.get(category_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Trouver tous les liens vers les livres dans la catégorie
        book_links = [link['href'] for link in soup.find_all('a') if 'catalogue' in link.get('href') and link.get('href').endswith('.html')]
        print(f"Liens des livres dans la catégorie {category_link}: {book_links}")

else:
    print(f"Erreur lors de la récupération de la page : {response.status_code}")
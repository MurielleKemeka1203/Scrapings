import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

def extract_book_details(book_url):
    """Extrait les détails d'un livre à partir de son URL.

    Args:
        book_url (str): L'URL de la page du livre.

    Returns:
        dict: Un dictionnaire contenant les détails du livre.
    """

    response = requests.get(book_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Adaptez les sélecteurs CSS en fonction de la structure HTML de la page
    title = soup.find('h1').text
    price = soup.find(class_="price_color").text.strip()
    author = soup.find("span", class_="author").text  
    
    # ... d'autres sélecteurs pour l'auteur, la description, les évaluations

    return {
        'title': title,
        'price': price,
        'author' : author, 
        # ... d'autres clés
    }

import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

# URL de la page
url = "http://books.toscrape.com/"

# Envoyer une requête HTTP GET à l'URL
response = requests.get(url)

# Vérifier si la requête a réussi (code de statut 200)
if response.status_code == 200:
    # Parser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Trouver   tous les liens vers les livres dans la catégorie
    book_links = [link['href'] for link in soup.find_all('a') if 'catalogue' in link.get('href') and link.get('href').endswith('.html')]
    # URL de la page d'accueil
    url = "http://books.toscrape.com/"


# Itérer sur chaque lien de livre
for book_link in book_links:
    book_url = url + book_link
    book_details = extract_book_details(book_url)
    print(book_details)



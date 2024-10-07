import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore
import csv

#(code pour extraire les données des livres)
#structure de données#
#Dictionnaire, chacun représentant un livre avec ses attributs(titre,auteurs....)

books_data = []
for book in books_data:
    book_data = {
        'title': book['title'],
        'author': book['author'],
        'price': book['price'],
        # ...
    }
    books_data.append(book_data)

#Fichier csv pour l'enrégistrement des données#

with open('books.csv', 'w', newline='') as csvfile:
    fieldnames = ['title', 'author', 'price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(books_data)


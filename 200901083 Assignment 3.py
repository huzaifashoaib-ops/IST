import xml.etree.ElementTree as ET
from openpyxl import Workbook

tree = ET.parse('compiler.xml')
root = tree.getroot()

workbook = Workbook()
sheet = workbook.active

sheet.append(["Book_id", "Author_Name", "Title", "Genre", "Price", "Publish_date", "Description"])

for book in root.findall('book'):
    book_id = book.get('id')
    author_name = book.find('author').text
    title = book.find('title').text
    genre = book.find('genre').text
    price = book.find('price').text
    publish_date = book.find('publish_date').text
    description = book.find('description').text

    print(f'Book_id: {book_id}')
    print(f'Author Name: {author_name}')
    print(f'Title: {title}')
    print(f'Genre: {genre}')
    print(f'Price: {price}')
    print(f'Publish_date: {publish_date}')
    print(f'Description: {description}')
    
    sheet.append([book_id, author_name, title, genre, price, publish_date, description])

workbook.save("books.xlsx")



import xml.dom.minidom

dom = xml.dom.minidom.parse('compiler.xml')
root = dom.documentElement
books = root.getElementsByTagName('book')
f = open('200901083 Assignment 3.xlsx', 'w')
for book in books:
    book_id = book.getAttribute('Book_Id')
    author_name_elements = book.getElementsByTagName('Author_Name')
    if author_name_elements:
        author_name = author_name_elements[0].firstChild.nodeValue
    else:
        author_name = ''
    title_elements = book.getElementsByTagName('Title')
    if title_elements:
        title = title_elements[0].firstChild.nodeValue
    else:
        title = ''
    genre_elements = book.getElementsByTagName('Genre')
    if genre_elements:
        genre = genre_elements[0].firstChild.nodeValue
    else:
        genre = ''
    price_elements = book.getElementsByTagName('Price')
    if price_elements:
        price = price_elements[0].firstChild.nodeValue
    else:
        price = ''
    publish_date_elements = book.getElementsByTagName('Publish_Date')
    if publish_date_elements:
        publish_date = publish_date_elements[0].firstChild.nodeValue
    else:
        publish_date = ''
    description_elements = book.getElementsByTagName('Description')
    if description_elements:
        description = description_elements[0].firstChild.nodeValue
    else:
        description = ''
    f.write(f"{book_id},{author_name},{title},{genre},{price},{publish_date},{description}\n")
f.close()
import json

def json_():

    books = [
    {
        "book": {
            "title": "The Great Gatsby",
            "cover": "Hardcover",
            "year": 1925,
            "pages": 180
        }
    },
    {
        "book": {
            "title": "To Kill a Mockingbird",
            "cover": "Paperback",
            "year": 1960,
            "pages": 281
        }
    },
    {
        "book": {
            "title": "1984",
            "cover": "Ebook",
            "year": 1949,
            "pages": 328
        }
    },
    {
        "book":{
            "title": "Harry Potter and the Philosopher's Stone",
            "cover": "Paperback",
            "year": 1997,
            "pages": 223
        }
    }
]
    print(books)

    with open("ex23.json", "w", encoding="utf-8") as f:
        json.dump(books, f, indent=2)

json_()

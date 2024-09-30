class Book:
    def __init__(self, title, author, genre, pub_date, read_date, rating, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pub_date = pub_date
        self.read_date = read_date
        self.rating = rating
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

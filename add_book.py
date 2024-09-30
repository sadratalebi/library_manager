from PyQt5 import QtWidgets, uic
from models.db_manager import DBManager

class AddBookWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AddBookWindow, self).__init__(parent)
        uic.loadUi('ui/add_book.ui', self)
        self.db = DBManager()

        self.save_button.clicked.connect(self.add_book)

    def add_book(self):
        title = self.title_input.text()
        author = self.author_input.text()
        genre = self.genre_input.text()
        pub_date = self.pub_date_input.text()
        read_date = self.read_date_input.text()
        rating = self.rating_input.text()
        pages = self.pages_input.text()

        if not title or not author:
            QtWidgets.QMessageBox.warning(self, "Error", "Title and Author are required")
            return

        self.db.add_book(title, author, genre, pub_date, read_date, rating, pages)
        self.parent().load_books()
        self.close()

from PyQt5 import QtWidgets, uic
from models.db_manager import DBManager
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui/main_window.ui', self)

        self.db = DBManager()

        # دکمه‌های اصلی
        self.add_button.clicked.connect(self.open_add_book)
        self.edit_button.clicked.connect(self.open_edit_book)
        self.delete_button.clicked.connect(self.delete_book)

        # لود کردن لیست کتاب‌ها
        self.load_books()

    def load_books(self):
        books = self.db.get_books()
        self.tableWidget.setRowCount(0)

        for row_number, book in enumerate(books):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(book):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def open_add_book(self):
        from ui.add_book import AddBookWindow
        self.add_book_window = AddBookWindow(self)
        self.add_book_window.show()

    def open_edit_book(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "No book selected")
            return

        book_id = self.tableWidget.item(selected_row, 0).text()
        from ui.edit_book import EditBookWindow
        self.edit_book_window = EditBookWindow(self, book_id)
        self.edit_book_window.show()

    def delete_book(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "No book selected")
            return

        book_id = self.tableWidget.item(selected_row, 0).text()
        self.db.delete_book(book_id)
        self.load_books()

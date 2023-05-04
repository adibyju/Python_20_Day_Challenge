import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import pyshorteners


class URLShortenerApp(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("URL Shortener App using Python")
        self.setGeometry(100, 100, 300, 300)

        # creating URL Entry label and Entry widget
        self.URLEntryLabel = QtWidgets.QLabel(self)
        self.URLEntryLabel.setText("Enter the URL to be shortened:")
        self.URLEntryLabel.adjustSize()

        self.URLEntryWidget = QtWidgets.QLineEdit(self)

        # creating Shortened URL label and display widget
        self.ShortenedURLLabel = QtWidgets.QLabel(self)
        self.ShortenedURLLabel.setText("The shortened URL is:")
        self.ShortenedURLLabel.adjustSize()

        self.ShortenedURLWidget = QtWidgets.QLineEdit(self)

        # button to shorten the URL
        self.ShortenURLButton = QtWidgets.QPushButton("Shorten URL")

        # create a vertical layout of all the components using QVBoxLayout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.URLEntryLabel)
        layout.addWidget(self.URLEntryWidget)
        layout.addWidget(self.ShortenedURLLabel)
        layout.addWidget(self.ShortenedURLWidget)
        layout.addWidget(self.ShortenURLButton)

        # set the layout to the main app
        self.setLayout(layout)

        # call shorten_URL_function() function when the button is clicked
        self.ShortenURLButton.clicked.connect(self.shorten_URL_function)

    # function to shorten the URL using pyshortener library
    def shorten_URL_function(self):
        shortenerObject = pyshorteners.Shortener()
        shortUrl = shortenerObject.tinyurl.short(self.URLEntryWidget.text())
        self.ShortenedURLWidget.setText(shortUrl)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainApp = URLShortenerApp()
    mainApp.show()
    sys.exit(app.exec_())

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.setCentralWidget(self.browser)

        # Navigation toolbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back, Forward, and Reload buttons
        navbar.addAction(QAction("Back", self, triggered=self.browser.back))
        navbar.addAction(QAction("Forward", self, triggered=self.browser.forward))
        navbar.addAction(QAction("Reload", self, triggered=self.browser.reload))

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.load_url)
        navbar.addWidget(self.url_bar)

        # Update URL bar when page changes
        self.browser.urlChanged.connect(lambda q: self.url_bar.setText(q.toString()))

    def load_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

app = QApplication(sys.argv)
window = Browser()
window.show()
sys.exit(app.exec_())
import os

from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QSizePolicy
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineHttpRequest
from PySide6.QtCore import Qt, QUrl

import KajunApplication


class KajunHomePage(QFrame):
    def __init__(self, owner: KajunApplication) -> None:
        super(KajunHomePage, self).__init__()

        # Don't change the function call order
        self.initialiseMemberVariables(owner)
        self.initialiseProperties()
        self.initialiseComponents()

    
    def initialiseMemberVariables(self, owner: KajunApplication) -> None:
        self.owner = owner


    def initialiseProperties(self) -> None:
        self.setFixedHeight(540)
        self.setStyleSheet(str("QFrame{ background-color: #2e2f33; color: #fbb03c; font: bold; font-size: 12px; }"))


    def initialiseComponents(self) -> None:
        # Page Layout 
        self.pageLayout = QVBoxLayout()
        self.pageLayout.setContentsMargins(20, 10, 20, 10)
        self.pageLayout.addSpacing(10)

        # Web Engine View
        self.webEngineView = QWebEngineView(parent=self)
        self.webEngineView.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
        self.webEngineView.load(QUrl().fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+ r"\My-Basic-Website\index.html"))
        self.pageLayout.addWidget(self.webEngineView)

        self.setLayout(self.pageLayout)
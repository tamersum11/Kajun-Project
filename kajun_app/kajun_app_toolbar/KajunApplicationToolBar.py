import os

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame, QLabel, QPushButton, QHBoxLayout, QSizePolicy, QSpacerItem
from PySide6.QtCore import QSize, Qt, QEvent, QObject

from kajun_app.BaseKajunApp import BaseKajunApp, Path


ImagesPath = os.path.join(Path, "images")


class KajunApplicationToolBar(QFrame):
    def __init__(self, owner: BaseKajunApp) -> None:
        super(KajunApplicationToolBar, self).__init__()

        # Don't change the function call order
        self.initialiseMemberVariables(owner)
        self.initialiseProperties()
        self.initialiseComponents()


    def initialiseMemberVariables(self, owner: BaseKajunApp) -> None:
        self.owner = owner


    def initialiseProperties(self) -> None:
        self.setFixedHeight(60)
        self.setStyleSheet(str("QFrame{ background-color: #26070a; color: #fbb03c; font: bold; font-size: 14px; }" +
                               "QPushButton{ background-color: #26070a; color: #fbb03c; font: bold; font-size: 14px; }" +
                               "QPushButton:hover{ background-color: #fbb03c; color: #26070a; }"))


    def initialiseComponents(self) -> None:
        # Icons
        self.setIcons()

        # Layout
        self.toolBarFrameLayout = QHBoxLayout()
        self.toolBarFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.toolBarFrameLayout.setSpacing(0)
        self.toolBarFrameLayout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        # Home Page Action
        self.homePageButton = QPushButton(self)
        self.homePageButton.setIcon(self.homePageIcon)
        self.homePageButton.setIconSize(QSize(60, 60))
        self.homePageButton.setObjectName("Home")
        self.homePageButton.installEventFilter(self)
        self.homePageButton.clicked.connect(self.owner.homePage)
        self.toolBarFrameLayout.addWidget(self.homePageButton)

        # Information Page Action
        self.infoPageButton = QPushButton(self)
        self.infoPageButton.setIcon(self.infoPageIcon)
        self.infoPageButton.setIconSize(QSize(60, 60))
        self.infoPageButton.setObjectName("Information")
        self.infoPageButton.installEventFilter(self)
        self.infoPageButton.clicked.connect(self.owner.informationPage)
        self.toolBarFrameLayout.addWidget(self.infoPageButton)

        # Vulnerabilities Page Action
        self.vulnerabilitiesPageButton = QPushButton(self)
        self.vulnerabilitiesPageButton.setIcon(self.vulnerabilitiesPageIcon)
        self.vulnerabilitiesPageButton.setIconSize(QSize(60, 60))
        self.vulnerabilitiesPageButton.setObjectName("Vulnerabilities")
        self.vulnerabilitiesPageButton.installEventFilter(self)
        self.vulnerabilitiesPageButton.clicked.connect(self.owner.vulnerabilitiesPage)
        self.toolBarFrameLayout.addWidget(self.vulnerabilitiesPageButton)

        # Spacer
        self.toolBarSpacerItem = QSpacerItem(60, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.toolBarFrameLayout.addSpacerItem(self.toolBarSpacerItem)

        # App Logo
        self.appLogo = QLabel()
        self.appLogo.setPixmap(self.appIcon)
        self.appLogo.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))
        self.appLogo.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.toolBarFrameLayout.addWidget(self.appLogo)

        self.setLayout(self.toolBarFrameLayout)


    def setIcons(self) -> None:
        self.homePageIcon = QPixmap(os.path.join(ImagesPath, "app-icons", "icons-kajun-yellow", "home.svg"))
        self.homePageIconHover = QPixmap(os.path.join(ImagesPath, "app-icons", "icons-kajun-purple", "home.svg"))
        self.infoPageIcon = QPixmap(os.path.join(ImagesPath, "app-icons", "icons-kajun-yellow", "terminal.svg"))
        self.infoPageIconHover = QPixmap(os.path.join(ImagesPath, "app-icons", "icons-kajun-purple", "terminal.svg"))
        self.vulnerabilitiesPageIcon = QPixmap(os.path.join(ImagesPath, "app-icons", "icons-kajun-yellow", "activity.svg"))
        self.vulnerabilitiesPageIconHover = QPixmap(os.path.join(ImagesPath, "app-icons", "icons-kajun-purple", "activity.svg"))
        self.appIcon = QPixmap(os.path.join(ImagesPath, "kajun_logo_60x60.png"))


    def eventFilter(self, object: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.HoverMove:
            text = object.objectName()
            if text == "Home":
                self.homePageButton.setText(text)
                self.homePageButton.setIcon(self.homePageIconHover)
            if text == "Information":
                self.infoPageButton.setText(text)
                self.infoPageButton.setIcon(self.infoPageIconHover)
            if text == "Vulnerabilities":
                self.vulnerabilitiesPageButton.setText(text)
                self.vulnerabilitiesPageButton.setIcon(self.vulnerabilitiesPageIconHover)

            return True
        elif event.type() == QEvent.Type.HoverLeave:
            text = object.objectName()
            if text == "Home":
                self.homePageButton.setText("")
                self.homePageButton.setIcon(self.homePageIcon)
            if text == "Information":
                self.infoPageButton.setText("")
                self.infoPageButton.setIcon(self.infoPageIcon)
            if text == "Vulnerabilities":
                self.vulnerabilitiesPageButton.setText("")
                self.vulnerabilitiesPageButton.setIcon(self.vulnerabilitiesPageIcon)

            return True

        return super(KajunApplicationToolBar, self).eventFilter(object, event)
import os

from PySide6.QtGui import QPixmap, QAction, QKeySequence
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy
from PySide6.QtCore import QSize, Qt

from BaseKajunApp import BaseKajunApp, KajunApplicationType, Path


class KajunApplication(BaseKajunApp):
    def __init__(self, app: QApplication) -> None:
        super(KajunApplication, self).__init__(app, KajunApplicationType.MAINWINDOW)

    
    def initialiseProperties(self) -> None:
        super(KajunApplication, self).initialiseProperties()
        self.setFixedSize(800, 600)
        self.setWindowTitle("Kajun Application")


    def initialiseComponents(self) -> None:
        super(KajunApplication, self).initialiseComponents()

        # Icons
        self.setIcons()

        # Pop-Up
        self.setPopUp()

        # ToolBar Frame
        self.setToolBarFrame()

        # Page Frame
        self.setPageFrame()
        
        self.centralLayout = QVBoxLayout()
        self.centralLayout.setContentsMargins(0, 0, 0, 0)
        self.centralLayout.addSpacing(0)
        self.centralLayout.addWidget(self.toolBarFrame)
        self.centralLayout.addWidget(self.pageFrame)
        self.setLayout(self.centralLayout)


    def setIcons(self) -> None:
        self.homePageIcon = QPixmap(os.path.join(Path, "images", "app-icons", "icons", "home-network.png"))
        self.infoPageIcon = QPixmap(os.path.join(Path, "images", "app-icons", "icons", "information-shield.png"))
        self.vulnerabilitiesPageIcon = QPixmap(os.path.join(Path, "images", "app-icons", "icons", "computer--exclamation.png"))
        self.appIcon = QPixmap(os.path.join(Path, "images", "kajun_logo_60x60.png"))


    def setPopUp(self) -> None:
        # Add Action to Pop-Up
        self.popup.addSeparator()

        # Home Page Action
        self.homePageAction = QAction(self.homePageIcon, "Home")
        self.homePageAction.setShortcut(QKeySequence("h"))
        self.homePageAction.triggered.connect(self.homePage)
        self.popup.addAction(self.homePageAction)

        # Information Page Action
        self.infoPageAction = QAction(self.infoPageIcon, "Information")
        self.infoPageAction.setShortcut(QKeySequence("i"))
        self.infoPageAction.triggered.connect(self.informationPage)
        self.popup.addAction(self.infoPageAction)

        # Vulnerabilities Page Action
        self.vulnerabilitiesPageAction = QAction(self.vulnerabilitiesPageIcon, "Vulnerabilities")
        self.vulnerabilitiesPageAction.setShortcut(QKeySequence("v"))
        self.vulnerabilitiesPageAction.triggered.connect(self.vulnerabilitiesPage)
        self.popup.addAction(self.vulnerabilitiesPageAction)  


    def setToolBarFrame(self) -> None:
        # ToolBar Frame
        self.toolBarFrame = QFrame()
        self.toolBarFrame.setFixedHeight(60)
        self.toolBarFrame.setStyleSheet(str("QFrame{ background-color: #26070a; color: #fbb03c; font: bold; font-size: 14px; }" + 
                                            "QPushButton{ background-color: #26070a; color: #fbb03c; font: bold; font-size: 14px; }" + 
                                            "QPushButton:hover{ background-color: #fbb03c; color: #26070a; }"))
        

        self.toolBarFrameLayout = QHBoxLayout()
        self.toolBarFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.toolBarFrameLayout.setSpacing(0)
        self.toolBarFrameLayout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        # Home Page Action
        self.homePageButton = QPushButton(self.toolBarFrame)
        self.homePageButton.setIcon(self.homePageIcon)
        self.homePageButton.setIconSize(QSize(60, 60))
        self.homePageButton.clicked.connect(self.homePage)
        self.toolBarFrameLayout.addWidget(self.homePageButton)

        # Information Page Action
        self.infoPageButton = QPushButton(self.toolBarFrame)
        self.infoPageButton.setIcon(self.infoPageIcon)
        self.infoPageButton.setIconSize(QSize(60, 60))
        self.infoPageButton.clicked.connect(self.informationPage)
        self.toolBarFrameLayout.addWidget(self.infoPageButton)

        # Vulnerabilities Page Action
        self.vulnerabilitiesPageButton = QPushButton(self.toolBarFrame)
        self.vulnerabilitiesPageButton.setIcon(self.vulnerabilitiesPageIcon)
        self.vulnerabilitiesPageButton.setIconSize(QSize(60, 60))
        self.vulnerabilitiesPageButton.clicked.connect(self.vulnerabilitiesPage)
        self.toolBarFrameLayout.addWidget(self.vulnerabilitiesPageButton)

        # App Logo
        self.appLogo = QLabel()
        self.appLogo.setPixmap(self.appIcon)
        self.appLogo.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))
        self.appLogo.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.toolBarFrameLayout.addWidget(self.appLogo)

        self.toolBarFrame.setLayout(self.toolBarFrameLayout)


    def setPageFrame(self) -> None:
        # Page Frame
        self.pageFrame = QFrame()
        self.pageFrame.setFixedHeight(540)
        self.pageFrame.setStyleSheet(str("QFrame{ background-color: #2e2f33; color: #fbb03c; font-size: 14px; }"))

        self.pageFrameLayout = QHBoxLayout()
        self.pageFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.pageFrameLayout.setSpacing(0)
        self.pageFrameLayout.setAlignment(Qt.AlignmentFlag.AlignBottom)

        self.pageFrame.setLayout(self.pageFrameLayout)


    def homePage(self) -> None:
        pass 


    def informationPage(self) -> None:
        pass 


    def vulnerabilitiesPage(self) -> None:
        pass 
        
from PySide6.QtGui import QAction, QKeySequence, QKeyEvent, QCloseEvent
from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt

from kajun_app.BaseKajunApp import BaseKajunApp
from kajun_app.KajunApplicationType import KajunApplicationType
from kajun_app.kajun_app_pages import KajunHomePage, KajunInformationPage, KajunVulnerabilitiesPage
from kajun_app.kajun_app_toolbar import KajunApplicationToolBar


class KajunApplication(BaseKajunApp):
    def __init__(self) -> None:
        super(KajunApplication, self).__init__(KajunApplicationType.MAINWINDOW)


    def initialiseProperties(self) -> None:
        super(KajunApplication, self).initialiseProperties()
        self.setFixedSize(900, 600)
        self.setWindowTitle("Kajun Application")


    def initialiseComponents(self) -> None:
        super(KajunApplication, self).initialiseComponents()

        # ToolBar Frame
        self.toolBarFrame = KajunApplicationToolBar(self)

        # Page Frame
        self.pageFrame = QFrame()
        self.pageFrame.setFixedHeight(540)
        self.pageFrame.setStyleSheet(str("QFrame{ background-color: #2e2f33; }"))

        self.pageFrameLayout = QHBoxLayout()
        self.pageFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.pageFrameLayout.setSpacing(0)
        self.pageFrameLayout.setAlignment(Qt.AlignmentFlag.AlignBottom)

        # Set Current Page
        self.currentPage = KajunHomePage(self)
        self.pageFrameLayout.addWidget(self.currentPage)
        self.pageFrame.setLayout(self.pageFrameLayout)

        # Set Layout
        self.centralLayout = QVBoxLayout()
        self.centralLayout.setContentsMargins(0, 0, 0, 0)
        self.centralLayout.addSpacing(0)
        self.centralLayout.addWidget(self.toolBarFrame)
        self.centralLayout.addWidget(self.pageFrame)
        self.setLayout(self.centralLayout)


    def initialisePopUpMenu(self) -> None:
        super(KajunApplication, self).initialisePopUpMenu()

        # Home Page Action
        self.homePageAction = QAction("Home")
        self.homePageAction.setShortcut(QKeySequence("h"))
        self.homePageAction.triggered.connect(self.homePage)
        self.popup.addAction(self.homePageAction)

        # Information Page Action
        self.infoPageAction = QAction("Information")
        self.infoPageAction.setShortcut(QKeySequence("i"))
        self.infoPageAction.triggered.connect(self.informationPage)
        self.popup.addAction(self.infoPageAction)

        # Vulnerabilities Page Action
        self.vulnerabilitiesPageAction = QAction("Vulnerabilities")
        self.vulnerabilitiesPageAction.setShortcut(QKeySequence("v"))
        self.vulnerabilitiesPageAction.triggered.connect(self.vulnerabilitiesPage)
        self.popup.addAction(self.vulnerabilitiesPageAction)


    def clearPageFrameLayout(self):
        for i in reversed(range(self.pageFrameLayout.count())):
            widget = self.pageFrameLayout.takeAt(i).widget()
            if widget is not None:
                widget.deleteLater()


    def homePage(self) -> None:
        self.clearPageFrameLayout()
        self.currentPage = KajunHomePage(self)
        self.pageFrameLayout.addWidget(self.currentPage)


    def informationPage(self) -> None:
        self.clearPageFrameLayout()
        self.currentPage = KajunInformationPage(self)
        self.pageFrameLayout.addWidget(self.currentPage)


    def vulnerabilitiesPage(self) -> None:
        self.clearPageFrameLayout()
        self.currentPage = KajunVulnerabilitiesPage(self)
        self.pageFrameLayout.addWidget(self.currentPage)


    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == 72:
            self.homePage()
        elif event.key() == 73:
            self.informationPage()
        elif event.key() == 86:
            self.vulnerabilitiesPage()
        else:
            super(KajunApplication, self).keyPressEvent(event)

    
    def closeEvent(self, event: QCloseEvent) -> None:
        self.hide()
        event.ignore()
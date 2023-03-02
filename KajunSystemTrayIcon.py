import os

from PySide6.QtGui import QPixmap, QMouseEvent, QCursor, QKeyEvent, QAction, QKeySequence
from PySide6.QtWidgets import QApplication, QMessageBox, QMenu, QSystemTrayIcon
from PySide6.QtCore import Qt, QEvent


Path = os.path.dirname(__file__)


class KajunSystemTrayIcon(QSystemTrayIcon):
    def __init__(self, app: QApplication) -> None:
        super(KajunSystemTrayIcon, self).__init__()

        # Don't change the function call order
        self.initialiseMemberVariables(app)
        self.initialiseComponents()
        self.initialisePopUpMenu() 
        self.initialiseProperties() 


    def initialiseMemberVariables(self, app: QApplication) -> None:
        self.app = app
        self.pixmap = QPixmap(os.path.join(Path, "images", "kajun_logo_60x60.png"))
    

    def initialiseComponents(self) -> None:
        # System Tray Icon
        self.setIcon(self.pixmap)

        # Pop-up
        self.popup = QMenu()
        self.popup.setStyleSheet(str("QMenu{ background-color: #2e2f33; color: #fbb03c; }" + 
                                    "QMenu::item:selected{ background-color: #fbb03c; color: #2e2f33; }"))


    def initialisePopUpMenu(self) -> None:
        # Pop-up Quit Action
        self.quitAction = QAction("Quit")
        self.quitAction.setShortcut(QKeySequence("q"))
        self.quitAction.triggered.connect(self.quit)
        self.popup.addAction(self.quitAction)

        self.popup.addSeparator()

        # Pop-up Reload Action
        self.reloadAction = QAction("Reload")
        self.reloadAction.setShortcut(QKeySequence("r"))
        # self.reloadAction.triggered.connect(self.close)
        self.popup.addAction(self.reloadAction)

        self.popup.addSeparator()

        # Pop-up Main Window Action
        self.mainWindowAction = QAction("Main Window")
        self.mainWindowAction.setShortcut(QKeySequence("m"))
        # self.mainWindowAction.triggered.connect(self.close)
        self.popup.addAction(self.mainWindowAction)

        self.setContextMenu(self.popup)


    def showInformation(self, text: str) -> None:
        self.showMessage("Information", text, QSystemTrayIcon.MessageIcon.Information, 3000)


    def initialiseProperties(self) -> None:
        self.setVisible(True)


    def quit(self) -> None:
        self.app.quit()
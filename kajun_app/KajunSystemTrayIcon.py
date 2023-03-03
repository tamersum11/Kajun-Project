import os

from PySide6.QtGui import QPixmap, QAction, QGuiApplication
from PySide6.QtWidgets import QApplication, QMenu, QSystemTrayIcon, QStyle
from PySide6.QtCore import Qt

from kajun_system_info.KajunSystemData import KajunSystemData
from kajun_app.KajunApplicationType import KajunApplicationType
from kajun_app.KajunAppFactory import KajunAppFactory
from kajun_app.BaseKajunApp import BaseKajunApp, Path


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
        self.systemInfo = []
        self.appFactory = KajunAppFactory()
        self.mainWindow = None
    

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
        self.quitAction.triggered.connect(self.quit)
        self.popup.addAction(self.quitAction)

        self.popup.addSeparator()

        # Pop-up Reload Action
        self.reloadAction = QAction("Reload")
        self.reloadAction.triggered.connect(self.reload)
        self.popup.addAction(self.reloadAction)
        
        self.popup.addSeparator()

        # Pop-up Main Window Action
        self.mainWindowAction = QAction("Main Window")
        self.mainWindowAction.triggered.connect(self.showMainWindow)
        self.popup.addAction(self.mainWindowAction)

        self.setContextMenu(self.popup)


    def showInformation(self, text: str) -> None:
        self.showMessage("Information", text, QSystemTrayIcon.MessageIcon.Information, 3000)


    def showWarning(self, text: str) -> None:
        self.showMessage("Warning", text, QSystemTrayIcon.MessageIcon.Warning, 3000)


    def initialiseProperties(self) -> None:
        self.setVisible(True)

    
    def showMainWindow(self) -> None:
        if self.mainWindow == None:
            self.mainWindow = self.appFactory.getKajunApplication(KajunApplicationType.MAINWINDOW)
            self.mainWindow.show()
        else:
            self.mainWindow.setVisible(True)
            self.mainWindow.setWindowState(Qt.WindowState.WindowMaximized)


    def newSystemInfoReceived(self, newSystemInfo: list[KajunSystemData]) -> None:
        warningtext = f"Date: {newSystemInfo[0].date}\nIp: {newSystemInfo[0].ip}\nDetail: {newSystemInfo[0].detail}"
        self.showWarning(warningtext)
        self.systemInfo.extend(newSystemInfo)
        self.reload()


    def reload(self) -> None:
        if self.mainWindow != None:
            self.mainWindow.setKajunSystemInfo(self.systemInfo)


    def setSystemInfo(self, systemInfo: list[KajunSystemData]) -> None:
        self.systemInfo = systemInfo


    def exec(self) -> int:
        return self.app.exec()


    def quit(self) -> None:
        self.app.quit()
from PySide6.QtWidgets import QApplication

from kajun_app.KajunAppFactory import KajunAppFactory 
from kajun_app.KajunApplicationType import KajunApplicationType
from kajun_app.BaseKajunApp import BaseKajunApp
from kajun_app.KajunSystemTrayIcon import KajunSystemTrayIcon

from kajun_app import DefaultInfoText, DefaultWarningText

from kajun_system_info.KajunSystemData import KajunSystemData


class BaseKajunProgress:
    def __init__(self, app: QApplication) -> None:
        # Don't change the function call order
        self.initialiseMemberVariables(app)


    def initialiseMemberVariables(self, app: QApplication) -> None:
        self.app = app
        self.systemTrayIcon = KajunSystemTrayIcon(self.app)
        self.appFactory = KajunAppFactory()

    
    def getKajunApplication(self, appType: KajunApplicationType) -> BaseKajunApp:
        return self.appFactory.getKajunApplication(appType)
    

    def getSystemData(self) -> list[KajunSystemData]:
        return list[KajunSystemData]


    def initialise(self) -> int:
        splash = self.getKajunApplication(KajunApplicationType.SPLASHSCREEN)
        systemData = self.getSystemData()
        splash.setKajunSystemInfo(systemData)
        splash.show()
        
        if splash.loadSystemInfo():
            self.systemTrayIcon.showInformation(DefaultInfoText)
            splash.close()
            mainWindow = self.getKajunApplication(KajunApplicationType.MAINWINDOW)
            mainWindow.show()
        else:
            splash.showWarning(DefaultWarningText)
            
        
        return self.systemTrayIcon.exec()
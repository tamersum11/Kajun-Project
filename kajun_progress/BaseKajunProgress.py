import threading
import time
import pandas as pd

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
        self.workerThread = threading.Thread(target=self.worker, daemon=True)
        self.systemTrayIcon = KajunSystemTrayIcon(self.app)
        self.appFactory = KajunAppFactory()

    
    def getKajunApplication(self, appType: KajunApplicationType) -> BaseKajunApp:
        return self.appFactory.getKajunApplication(appType)
    

    def getSystemData(self) -> list[KajunSystemData]:
        return list[KajunSystemData]
    

    def checkVulnerabilities(self) -> list[KajunSystemData]:
        return list[KajunSystemData]


    def worker(self) -> None:
        while True:
            time.sleep(10.0)
            newSystemInfo = self.checkVulnerabilities()
            try:
                if newSystemInfo[0] != None:
                    self.systemTrayIcon.newSystemInfoReceived(newSystemInfo)
            except:
                continue
                


    def initialise(self) -> int:
        # Load System Data
        systemData = self.getSystemData()
        self.systemTrayIcon.setSystemInfo(systemData)

        # Start Worker Thread
        self.workerThread.start()

        # Load Splash
        splash = self.getKajunApplication(KajunApplicationType.SPLASHSCREEN)
        splash.setKajunSystemInfo(systemData)
        splash.show()
        
        if splash.loadSystemInfo():
            self.systemTrayIcon.showInformation(DefaultInfoText)
            splash.close()
            self.systemTrayIcon.showMainWindow()
        else:
            splash.showWarning(DefaultWarningText)
            
        
        return self.systemTrayIcon.exec()
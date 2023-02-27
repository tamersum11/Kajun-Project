from PySide6.QtWidgets import QApplication, QLabel, QProgressBar

from KajunAppFactory import KajunAppFactory, BaseKajunApp, KajunApplicationType
from BaseKajunApp import  DefaultInfoText, DefaultWarningText


class BaseProgress:
    def __init__(self, app: QApplication) -> None:
        self.app = app
        self.appFactory = KajunAppFactory(app)

    
    def setInfoLabel(self, infoLabel: QLabel) -> None:
        self.infoLabel = infoLabel


    def setProgressBar(self, progressBar: QProgressBar) -> None:
        self.progressBar = progressBar


    def setKajunApplication(self, kajunApp: BaseKajunApp) -> None:
        self.kajunApp = kajunApp

    
    def getKajunApplication(self, appType: KajunApplicationType) -> BaseKajunApp:
        return self.appFactory.getKajunApplication(appType)


    def initialise(self) -> int:
        return -1


    def startSplashScreenProgress(self) -> bool:
        return False
    

    def startMainWindowProgress(self) -> bool:
        return False
    

    def startProgress(self, appType: KajunApplicationType) -> bool:
        if appType == KajunApplicationType.SPLASHSCREEN:
            return self.startSplashScreenProgress()
        elif appType == KajunApplicationType.MAINWINDOW:
            return self.startMainWindowProgress()
        else:
            return False


    def restartSplashScreenProgress(self) -> int:
        return -1
    

    def restartMainWindowProgress(self) -> int:
        return -1


    def restartProgress(self, appType: KajunApplicationType) -> int:
        if appType == KajunApplicationType.SPLASHSCREEN:
            return self.restartSplashScreenProgress()
        elif appType == KajunApplicationType.MAINWINDOW:
            return self.restartMainWindowProgress()
        else:
            return -1
    

    def stopSplashScreenProgress(self) -> int:
        return -1
    

    def stopMainWindowProgress(self) -> int:
        return -1


    def stopProgress(self, appType: KajunApplicationType) -> int:
        if appType == KajunApplicationType.SPLASHSCREEN:
            return self.stopSplashScreenProgress()
        elif appType == KajunApplicationType.MAINWINDOW:
            return self.stopMainWindowProgress()


    def splashScreenProgressSuccess(self) -> int:
        self.kajunApp.showInformation(DefaultInfoText)
        self.kajunApp.close()

        # Main Window
        mainWindow = self.getKajunApplication(KajunApplicationType.MAINWINDOW)
        self.setKajunApplication(mainWindow)
        self.kajunApp.setBaseProgress(self)
        self.kajunApp.show()

        return -1


    def checkProgressStatus(self, status: bool) -> int:        
        if status:
            appType = self.kajunApp.getApplicationType()
            
            if appType == KajunApplicationType.SPLASHSCREEN:
                return self.splashScreenProgressSuccess()
            elif appType == KajunApplicationType.MAINWINDOW:
                return self.stopMainWindowProgress()
        else:
            return self.kajunApp.showWarning(DefaultWarningText)
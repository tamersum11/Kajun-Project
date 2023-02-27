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


    def restartSplashScreenProgress(self) -> bool:
        return False
    

    def restartMainWindowProgress(self) -> bool:
        return False


    def restartProgress(self, appType: KajunApplicationType) -> bool:
        if appType == KajunApplicationType.SPLASHSCREEN:
            return self.restartSplashScreenProgress()
        elif appType == KajunApplicationType.MAINWINDOW:
            return self.restartMainWindowProgress()
        else:
            return False
    

    def stopSplashScreenProgress(self) -> None:
        pass
    

    def stopMainWindowProgress(self) -> None:
        pass


    def stopProgress(self, appType: KajunApplicationType) -> None:
        if appType == KajunApplicationType.SPLASHSCREEN:
            self.stopSplashScreenProgress()
        elif appType == KajunApplicationType.MAINWINDOW:
            self.stopMainWindowProgress()


    def splashScreenProgressSuccess(self) -> None:
        self.kajunApp.showInformation(DefaultInfoText)
        self.kajunApp.close()

        # Main Window
        mainWindow = self.getKajunApplication(KajunApplicationType.MAINWINDOW)
        self.setKajunApplication(mainWindow)
        self.kajunApp.setBaseProgress(self)
        self.kajunApp.show()


    def checkProgressStatus(self, status: bool) -> None:
        appType = self.kajunApp.getApplicationType()
        
        if status:
            if appType == KajunApplicationType.SPLASHSCREEN:
                self.splashScreenProgressSuccess()
            elif appType == KajunApplicationType.MAINWINDOW:
                self.stopMainWindowProgress()
        else:
            self.kajunApp.showWarning(DefaultWarningText)
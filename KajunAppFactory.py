
from PySide6.QtWidgets import QApplication

from BaseKajunApp import BaseKajunApp, KajunApplicationType
from KajunSplashScreen import KajunSplashScreen
from KajunApplication import KajunApplication


class KajunAppFactory:
    def __init__(self, app: QApplication) -> None:
        self.app = app


    def getKajunApplication(self, appType: KajunApplicationType) -> BaseKajunApp:
        if appType == KajunApplicationType.SPLASHSCREEN:
            return KajunSplashScreen(self.app)
        elif appType == KajunApplicationType.MAINWINDOW:
            return KajunApplication(self.app)
        else:
            return BaseKajunApp(self.app, KajunApplicationType.NONE)
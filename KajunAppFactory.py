
from BaseKajunApp import BaseKajunApp, KajunApplicationType
from KajunSplashScreen import KajunSplashScreen
from KajunApplication import KajunApplication


class KajunAppFactory:
    def __init__(self) -> None:
        pass


    def getKajunApplication(self, appType: KajunApplicationType) -> BaseKajunApp:
        if appType == KajunApplicationType.SPLASHSCREEN:
            return KajunSplashScreen()
        elif appType == KajunApplicationType.MAINWINDOW:
            return KajunApplication()
        else:
            return BaseKajunApp(KajunApplicationType.NONE)
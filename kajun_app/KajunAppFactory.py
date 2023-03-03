from kajun_app.BaseKajunApp import BaseKajunApp
from kajun_app.KajunApplicationType import KajunApplicationType
from kajun_app.KajunSplashScreen import KajunSplashScreen
from kajun_app.KajunApplication import KajunApplication


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
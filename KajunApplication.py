from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication

from BaseKajunApp import BaseKajunApp, KajunApplicationType


class KajunApplication(BaseKajunApp):
    def __init__(self, app: QApplication) -> None:
        super(KajunApplication, self).__init__(app, KajunApplicationType.MAINWINDOW)


    def initialiseProperties(self) -> None:
        super(KajunApplication, self).initialiseProperties()
        self.setFixedSize(800, 600)
        self.setWindowTitle("Kajun Application")


    def initialiseComponents(self) -> None:
        super(KajunApplication, self).initialiseComponents()



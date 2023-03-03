import os
import sys

from PySide6.QtGui import QPixmap, QMouseEvent, QCursor, QKeyEvent, QAction, QKeySequence
from PySide6.QtWidgets import QWidget, QMessageBox, QMenu
from PySide6.QtCore import Qt, QEvent

from kajun_system_info.KajunSystemData import KajunSystemData
from kajun_app.KajunApplicationType import KajunApplicationType


Path = sys.path[0]
DefaultInfoText = str("Progress is successfully done.")
DefaultWarningText = str("Progress failed unexpectedly!")


class BaseKajunApp(QWidget):
    def __init__(self, appType: KajunApplicationType) -> None:
        super(BaseKajunApp, self).__init__()

        # Don't change the function call order
        self.initialiseMemberVariables(appType)
        self.initialiseProperties()
        self.initialiseComponents()
        self.initialisePopUpMenu()


    def initialiseMemberVariables(self, appType: KajunApplicationType) -> None:
        self.appType = appType
        self.kajunSystemInfo = list[KajunSystemData]
        self.pixmap = QPixmap(os.path.join(Path, "images", "kajun_logo.png"))


    def initialiseProperties(self) -> None:
        self.setWindowIcon(self.pixmap)
        self.setStyleSheet("background-color: #2e2f33; color: #fbb03c; ")


    def initialiseComponents(self) -> None:
        # Pop-up
        self.popup = QMenu()
        self.popup.setStyleSheet(str("QMenu{ background-color: #2e2f33; color: #fbb03c; }" +
                                     "QMenu::item:selected{ background-color: #fbb03c; color: #2e2f33; }"))


    def initialisePopUpMenu(self) -> None:
        # Pop-up Close Action
        self.quitAction = QAction("Close")
        self.quitAction.setShortcut(QKeySequence("c"))
        self.quitAction.triggered.connect(self.close)
        self.popup.addAction(self.quitAction)

        self.popup.addSeparator()


    def showInformation(self, text: str) -> int:
        messageBox = QMessageBox(self)
        messageBox.setWindowTitle("Information")
        messageBox.setText(text)
        messageBox.setIcon(QMessageBox.Icon.Information)
        messageBox.setStyleSheet(
            str("QPushButton{ background-color: grey; color: #fbb03c; border-width: 4px; border-color: #fbb03c; }" +
                "QPushButton::hover{ background-color: #fbb03c; color: #2e2f33; }"))
        messageBox.setStandardButtons(QMessageBox.StandardButton.Ok)

        return messageBox.exec()


    def showWarning(self, text: str) -> int:
        messageBox = QMessageBox(self)
        messageBox.setWindowTitle("Error")
        messageBox.setText(text)
        messageBox.setIcon(QMessageBox.Icon.Critical)
        messageBox.setStyleSheet(
            str("QPushButton{ background-color: grey; color: #fbb03c; border-width: 4px; solid; border-color: #fbb03c; }" +
                "QPushButton::hover{ background-color: #fbb03c; color: #2e2f33; }"))
        messageBox.setStandardButtons(QMessageBox.StandardButton.Ok)

        return messageBox.exec()


    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.type() == QEvent.Type.MouseButtonPress:
            if event.button() == Qt.MouseButton.LeftButton:
                self.popup.close()
            if event.button() == Qt.MouseButton.RightButton:
                currentMouseCursor = QCursor.pos()
                self.popup.move(currentMouseCursor)
                self.popup.show()

        super(BaseKajunApp, self).mousePressEvent(event)


    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == 67:
            self.close()
        else:
            super(BaseKajunApp, self).keyPressEvent(event)


    def getApplicationType(self) -> KajunApplicationType:
        return self.appType
    

    def setKajunSystemInfo(self, kajunSystemInfo: list[KajunSystemData]) -> None:
        self.kajunSystemInfo = kajunSystemInfo


    def getKajunSystemInfo(self) -> list[KajunSystemData]:
        return self.kajunSystemInfo
    
    
    def loadSystemInfo(self) -> bool:
        return False
    

    def homePage(self) -> None:
        pass


    def informationPage(self) -> None:
        pass


    def vulnerabilitiesPage(self) -> None:
        pass
import os
import enum

from PySide6.QtGui import QPixmap, QMouseEvent, QCursor, QKeyEvent, QAction, QKeySequence
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QMenu
from PySide6.QtCore import Qt, QEvent

import BaseProgress


Path = os.path.dirname(__file__)
DefaultInfoText = str("Progress is successfully done.")
DefaultWarningText = str("Progress failed unexpectedly!")


class KajunApplicationType(enum.Enum):
        SPLASHSCREEN    = 0
        MAINWINDOW      = 1
        NONE            = 2


class BaseKajunApp(QWidget):
    def __init__(self, app: QApplication, appType: KajunApplicationType) -> None:
        super(BaseKajunApp, self).__init__()

         # Don't change the function call order
        self.initialiseMemberVariables(app, appType)
        self.initialiseProperties() 
        self.initialiseComponents()
        self.initialisePopUpMenu()   

    
    def initialiseMemberVariables(self, app: QApplication, appType: KajunApplicationType) -> None:
        self.app = app
        self.appType = appType
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
        # Pop-up Quit Action
        self.quitAction = QAction("Close")
        self.quitAction.setShortcut(QKeySequence("c"))
        self.quitAction.triggered.connect(self.quit)
        self.popup.addAction(self.quitAction)

        self.popup.addSeparator()


    def showInformation(self, text: str) -> int:
        messageBox = QMessageBox(self)
        messageBox.setWindowTitle("Information")
        messageBox.setText(text)
        messageBox.setIcon(QMessageBox.Icon.Information)
        messageBox.setStyleSheet(str("QPushButton{ background-color: grey; color: #fbb03c; border-width: 4px; border-color: #fbb03c; }" +
                                    "QPushButton::hover{ background-color: #fbb03c; color: #2e2f33; }"))
        messageBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        
        return messageBox.exec()

    
    def showWarning(self, text: str) -> int:
        messageBox = QMessageBox(self)
        messageBox.setWindowTitle("Error")
        messageBox.setText(text)
        messageBox.setIcon(QMessageBox.Icon.Critical)
        messageBox.setStyleSheet(str("QPushButton{ background-color: grey; color: #fbb03c; border-width: 4px; solid; border-color: #fbb03c; }" +
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
                self.quit()
            elif event.key() == 82:
                self.startProgress()
            elif event.key() == 83:
                self.stopProgress()
                pass
            else:
                super(BaseKajunApp, self).keyPressEvent(event)      

    
    def getApplicationType(self) -> KajunApplicationType:
        return self.appType


    def setProgressProperties(self) -> None:
        pass


    def setBaseProgress(self, progress: BaseProgress) -> None:
        self.progress = progress
        self.setProgressProperties()


    def startProgress(self) -> bool:
        return self.progress.startProgress(self.appType)
    

    def restartProgress(self) -> int:
        return self.progress.restartProgress(self.appType)
    

    def stopProgress(self) -> int:
        self.progress.stopProgress(self.appType)


    def quit(self) -> None:
        self.app.quit()

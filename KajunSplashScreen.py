import os
from time import sleep

from PySide6.QtGui import QAction, QPixmap, QMouseEvent, QKeyEvent, QCursor, QKeySequence
from PySide6.QtWidgets import QApplication, QWidget, QMenu, QFrame, QVBoxLayout, QLabel, QProgressBar, QMessageBox, QLayout
from PySide6.QtCore import Qt, QEvent

path = os.path.dirname(__file__)

defaultInfoText = str("Progress is successfully done.")

defaultWarningText = str("Progress can not start!")

class KajunSplashScreen(QWidget):
    def __init__(self, app: QApplication) -> None:
        super(KajunSplashScreen, self).__init__()
        
        # Don't change the function call order
        self.initialiseMemberVariables(app)
        self.initialiseProperties()
        self.initialiseComponents()
        self.keyReleaseEvent
        
    def initialiseMemberVariables(self, app: QApplication) -> None:
        self.app = app
        self.pixmap = QPixmap(os.path.join(path, "images", "kajun_logo.png"))

    def initialiseProperties(self) -> None:
        self.setWindowIcon(self.pixmap)
        self.setWindowFlags(Qt.WindowType.SplashScreen | Qt.WindowType.WindowStaysOnTopHint)
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #2e2f33; color: #fbb03c; ")

    def initialiseComponents(self) -> None:
        # Pop-up
        self.popup = QMenu()
        self.popup.setStyleSheet(str("QMenu{ background-color: #2e2f33; color: #fbb03c; }" + 
                                    "QMenu::item:selected{ background-color: #fbb03c; color: #2e2f33; }"))

        # Pop-up Quit Action
        self.quitAction = QAction("Close")
        self.quitAction.setShortcut(QKeySequence("q"))
        self.quitAction.triggered.connect(self.quit)
        self.popup.addAction(self.quitAction)

        self.popup.addSeparator()

        # Pop-up Start Progress Action
        self.restartProgressAction = QAction("Restart Progress")
        self.restartProgressAction.setShortcut(QKeySequence("r"))
        self.restartProgressAction.triggered.connect(self.startProgress)
        self.popup.addAction(self.restartProgressAction)

        # Pop-up Stop Progress Action
        self.stopProgressAction = QAction("Stop Progress")
        self.stopProgressAction.setShortcut(QKeySequence("s"))
        # self.stopProgressAction.triggered.connect(self.stopProgress)
        self.popup.addAction(self.stopProgressAction)

        # Image Component
        self.image = QLabel()
        self.image.setPixmap(self.pixmap)
        self.image.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        # Image Frame
        self.imageFrame = QFrame()
        self.imageFrameLayout = QVBoxLayout()
        self.imageFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.imageFrameLayout.addWidget(self.image)
        self.imageFrame.setLayout(self.imageFrameLayout)

        # Title Label Component
        self.titleLabel = QLabel()
        self.titleLabel.setText("Kajun Application")
        self.titleLabel.setStyleSheet("color: #fbb03c; font: bold; font-size: 14px;")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        # Subtitle Label Component
        self.subtitleLabel = QLabel()
        self.subtitleLabel.setText("Kajun Application Splash Screen")
        self.subtitleLabel.setStyleSheet("color: #fbb03c; font: bold; font-size: 10px;")
        self.subtitleLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        # ProgressBar Component
        self.progressBar = QProgressBar()
        self.progressBar.setStyleSheet(str("QProgressBar{ border: 10px; border-color: #fbb03c; background-color: grey; color: #2e2f33; font: bold; }" + 
                                            "QProgressBar::chunk{ background-color: #fbb03c;}"))
        
        self.progressBar.setFixedSize(360, 16)
        self.progressBar.setRange(0, 100)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        # Info Label Component
        self.infoLabel = QLabel()
        self.infoLabel.setText("Test Text")
        self.infoLabel.setStyleSheet("color: #fbb03c; font-size: 10px;")
        self.infoLabel.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Info Frame
        self.infoFrame = QFrame()        
        self.infoFrameLayout = QVBoxLayout()
        self.infoFrameLayout.addWidget(self.titleLabel)
        self.infoFrameLayout.addWidget(self.subtitleLabel)
        self.infoFrameLayout.addWidget(self.progressBar)
        self.infoFrameLayout.addWidget(self.infoLabel)
        self.infoFrameLayout.setContentsMargins(20, 0, 20, 0)
        self.infoFrameLayout.setSpacing(0)
        self.infoFrame.setFixedHeight(100)
        self.infoFrameLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.infoFrame.setLayout(self.infoFrameLayout)

        # Add frames to Layout
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.addWidget(self.imageFrame)
        self.verticalLayout.addWidget(self.infoFrame)
        self.setLayout(self.verticalLayout)
    
    def startProgress(self) -> None:
        for progress in range(100):
            sleep(0.05)
            info = str("Lorem ipsum dolor sit amet, consectetur adipiscing elit. \n" +
                       f"Test Progress Info Label Progress Id: {progress + 1}")
            self.infoLabel.setText(info)
            self.progressBar.setValue(progress + 1)

        self.showInformation(defaultInfoText)    
            
        # self.showWarning(defaultWarningText)

    def showInformation(self, text: str) -> None:
        messageBox = QMessageBox(self)
        messageBox.setWindowTitle("Information")
        messageBox.setText(text)
        messageBox.setIcon(QMessageBox.Icon.Information)
        messageBox.setStyleSheet(str("QPushButton{ background-color: grey; color: #fbb03c; border-width: 4px; border-color: #fbb03c; }" +
                                    "QPushButton::hover{ background-color: #fbb03c; color: #2e2f33; }"))
        messageBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        messageBox.exec()
    
    def showWarning(self, text: str) -> None:
        messageBox = QMessageBox(self)
        messageBox.setWindowTitle("Error")
        messageBox.setText(text)
        messageBox.setIcon(QMessageBox.Icon.Critical)
        messageBox.setStyleSheet(str("QPushButton{ background-color: grey; color: #fbb03c; border-width: 4px; solid; border-color: #fbb03c; }" +
                                    "QPushButton::hover{ background-color: #fbb03c; color: #2e2f33; }"))
        messageBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        messageBox.exec()
    
    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.type() == QEvent.Type.MouseButtonPress:
            if event.button() == Qt.MouseButton.LeftButton:
                self.popup.close()
            if event.button() == Qt.MouseButton.RightButton:
                currentMouseCursor = QCursor.pos()
                self.popup.move(currentMouseCursor)
                self.popup.show()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == 81:
            self.quit()
        elif event.key() == 82:
            self.startProgress()
        elif event.key() == 83:
            # self.stopProgress()
            pass
        else:
            super(KajunSplashScreen, self).keyPressEvent(event)

    def quit(self) -> None:
        self.app.quit()
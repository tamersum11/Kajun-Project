import os
from time import sleep

from PySide6.QtGui import QAction, QPixmap, QMouseEvent, QCursor
from PySide6.QtWidgets import QApplication, QWidget, QMenu, QFrame, QVBoxLayout, QLabel, QProgressBar, QMessageBox
from PySide6.QtCore import Qt, QEvent

path = os.path.dirname(__file__)

progressBarStyleSheet = str("QProgressBar { border: 10px; border-color: #fbb03c; background-color: grey; }" + 
                            "QProgressBar::chunk { background-color: #fbb03c;}")

class Application(QWidget):
    def __init__(self, app: QApplication) -> None:
        super(Application, self).__init__()
        
        # Don't change the function call order
        self.initialiseMemberVariables(app)
        self.initialiseProperties()
        self.initialiseComponents()
        
    def initialiseMemberVariables(self, app: QApplication) -> None:
        self.app = app

    def initialiseProperties(self) -> None:
        self.setWindowFlags(Qt.WindowType.CustomizeWindowHint)
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #2e2f33; color: #fbb03c")

    def initialiseComponents(self) -> None:
        # Pop-up
        self.popup = QMenu()
        self.popup.setStyleSheet("background-color: #2e2f33; color: #fbb03c")

        # Pop-up Quit Action
        self.quitAction = QAction("Close")
        self.quitAction.triggered.connect(self.quit)
        self.popup.addAction(self.quitAction)

        # Pop-up Start Progress Action
        self.startProgressAction = QAction("Start Progress")
        self.startProgressAction.triggered.connect(self.startProgress)
        self.popup.addAction(self.startProgressAction)

        # Pop-up Stop Progress Action
        self.stopProgressAction = QAction("Stop Progress")
        # self.stopProgressAction.triggered.connect(self.stopProgress)
        self.popup.addAction(self.stopProgressAction)

        # Image Component
        self.image = QLabel()
        pixmap = QPixmap(os.path.join(path, "images", "kajun_logo.png"))
        self.image.setPixmap(pixmap)
        self.image.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        # Image Frame
        self.imageFrame = QFrame()
        self.imageFrameLayout = QVBoxLayout()
        self.imageFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.imageFrameLayout.addWidget(self.image)
        self.imageFrame.setLayout(self.imageFrameLayout)

        # Info Label Component
        self.infoLabel = QLabel()
        self.infoLabel.setText("Test Text")
        self.infoLabel.setStyleSheet("color: #fbb03c")

        # ProgressBar Component
        self.progressBar = QProgressBar()
        self.progressBar.setStyleSheet(progressBarStyleSheet)
        self.progressBar.setRange(0, 100)
        self.progressBar.setValue(50)

        # Info Frame
        self.infoFrame = QFrame()
        self.infoFrameLayout = QVBoxLayout()
        self.infoFrameLayout.setContentsMargins(20, 20, 20, 20)
        self.infoFrameLayout.addWidget(self.infoLabel)
        self.infoFrameLayout.addWidget(self.progressBar)
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
            self.infoLabel.setText(f"Test Progress Info Label Progress Id: {progress + 1}")
            self.progressBar.setValue(progress + 1)
            
        self.showWarning()
    
    def showWarning(self) -> None:
        messageBox = QMessageBox()
        messageBox.setWindowTitle("Error")
        messageBox.setText("Progress can not start!")
        messageBox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        messageBox.setIcon(QMessageBox.Icon.Critical)
        button = messageBox.exec_()

        if button == QMessageBox.StandardButton.Cancel:
            self.quit()
    
    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.type() == QEvent.Type.MouseButtonPress:
            if event.button() == Qt.MouseButton.LeftButton:
                self.popup.close()
            if event.button() == Qt.MouseButton.RightButton:
                currentMouseCursor = QCursor.pos()
                self.popup.move(currentMouseCursor)
                self.popup.show()
    
    def quit(self) -> None:
        self.app.quit()
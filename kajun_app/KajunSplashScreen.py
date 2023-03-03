import os
from time import sleep

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QProgressBar, QLayout
from PySide6.QtCore import Qt

from kajun_app.BaseKajunApp import BaseKajunApp, Path
from kajun_app.KajunApplicationType import KajunApplicationType


class KajunSplashScreen(BaseKajunApp):
    def __init__(self) -> None:
        super(KajunSplashScreen, self).__init__(KajunApplicationType.SPLASHSCREEN)


    def initialiseProperties(self) -> None:
        super(KajunSplashScreen, self).initialiseProperties()
        self.setWindowFlags(Qt.WindowType.SplashScreen | Qt.WindowType.WindowStaysOnTopHint)
        self.setFixedSize(400, 300)


    def initialiseComponents(self) -> None:
        super(KajunSplashScreen, self).initialiseComponents()

        # Image Component
        self.image = QLabel()
        self.image.setPixmap(QPixmap(os.path.join(Path, "images", "kajun_logo_splash.png")))
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

    
    def loadSystemInfo(self) -> bool:
        for progress in range(1, 101):
            sleep(0.05)

            info = str("Lorem ipsum dolor sit amet, consectetur adipiscing elit. \n" +
                       f"Test Progress Info Label Progress Id: {progress}")
            self.infoLabel.setText(info)
            self.progressBar.setValue(progress)
                    
        return True
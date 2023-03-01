from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

import KajunApplication


class KajunVulnerabilitiesPage(QFrame):
    def __init__(self, owner: KajunApplication) -> None:
        super(KajunVulnerabilitiesPage, self).__init__()

        # Don't change the function call order
        self.initialiseMemberVariables(owner)
        self.initialiseProperties()
        self.initialiseComponents()

    
    def initialiseMemberVariables(self, owner: KajunApplication) -> None:
        self.owner = owner


    def initialiseProperties(self) -> None:
        self.setFixedHeight(540)
        self.setStyleSheet(str("QFrame{ background-color: #2e2f33; color: #fbb03c; font: bold; font-size: 12px; }"))


    def initialiseComponents(self) -> None:
        # Page Layout 
        self.pageLayout = QVBoxLayout()
        self.pageLayout.setContentsMargins(20, 10, 20, 10)
        self.pageLayout.addSpacing(10)

        #Test Label
        self.titleLabel = QLabel("Kajun Vulnerabilities Page")
        self.titleLabel.setStyleSheet("font-size: 24px;")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.pageLayout.addWidget(self.titleLabel)

        self.setLayout(self.pageLayout)
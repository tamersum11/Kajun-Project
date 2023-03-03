from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QTableWidget, QHeaderView, QTableWidgetItem
from PySide6.QtCore import Qt

from kajun_app.BaseKajunApp import BaseKajunApp


class KajunVulnerabilitiesPage(QFrame):
    def __init__(self, owner: BaseKajunApp) -> None:
        super(KajunVulnerabilitiesPage, self).__init__()

        # Don't change the function call order
        self.initialiseMemberVariables(owner)
        self.initialiseProperties()
        self.initialiseComponents()
        self.loadTable()


    def initialiseMemberVariables(self, owner: BaseKajunApp) -> None:
        self.owner = owner
        self.tableWidgetTitle = ["ID", "Date-Time", "Ip-Address", "Detail"]


    def initialiseProperties(self) -> None:
        self.setFixedHeight(540)
        self.setStyleSheet(str("QFrame{ background-color: #2e2f33; color: #fbb03c; font: bold; font-size: 12px; }"))


    def initialiseComponents(self) -> None:
        # Page Layout
        self.pageLayout = QVBoxLayout()
        self.pageLayout.setContentsMargins(20, 10, 20, 10)
        self.pageLayout.addSpacing(10)

        # Test Label
        self.titleLabel = QLabel("Kajun Vulnerabilities Page")
        self.titleLabel.setStyleSheet("font-size: 24px;")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.pageLayout.addWidget(self.titleLabel)

        # Table Widget
        self.tableWidget = QTableWidget(0, 4)

        self.verticalheader = QHeaderView(Qt.Orientation.Vertical)
        self.tableWidget.setVerticalHeader(self.verticalheader)
        self.horizontalheader = QHeaderView(Qt.Orientation.Horizontal)
        self.tableWidget.setHorizontalHeader(self.horizontalheader)
        self.tableWidget.setHorizontalHeaderLabels(self.tableWidgetTitle)
        self.pageLayout.addWidget(self.tableWidget)

        self.setLayout(self.pageLayout)

    
    def loadTable(self) -> None:
        systemInfo = self.owner.getKajunSystemInfo()
        i = 0
        while True:
            try:
                data = systemInfo[i]
                for j in range(4):
                    if j == 0:
                        item = QTableWidgetItem(str(data.id))
                        self.tableWidget.setItem(i, j, item)
                    if j == 1:
                        item = QTableWidgetItem(data.date)
                        self.tableWidget.setItem(i, j, item)
                    if j == 2:
                        item = QTableWidgetItem(data.ip)
                        self.tableWidget.setItem(i, j, item)
                    if j == 3:
                        item = QTableWidgetItem(data.detail)
                        self.tableWidget.setItem(i, j, item)
            except:
                break

            i += 1

import random
import socket
from datetime import datetime

from PySide6.QtWidgets import QApplication

from kajun_progress.BaseKajunProgress import BaseKajunProgress
from kajun_system_info.KajunSystemData import KajunSystemData


class TestProgress(BaseKajunProgress):
    def __init__(self, app: QApplication) -> None:
        super(TestProgress, self).__init__(app)

        self.id = 1

    
    def getProgressStatus(self) -> bool:
        status = random.randint(-1, 1)
        return status == 1
    

    def getVulnerabilitiesNumber(self) -> int:
        return random.randint(1, 5)


    def getIpAddress(self) -> str:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    

    def getDateTime(self) -> str:
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M:%S")
    

    def generateVulnerabilities(self, limit: int) -> list[KajunSystemData]:
        systemDataList = []

        ip = self.getIpAddress()
        date = self.getDateTime()
        detail = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

        for i in range(1, limit):         
            systemDataList.append(KajunSystemData(self.id, date, ip, detail))
            self.id += 1

        return systemDataList 


    def checkVulnerabilities(self) -> list[KajunSystemData]:
        if self.getProgressStatus():
            numOFVulnerabilities = self.getVulnerabilitiesNumber()
            return self.generateVulnerabilities(numOFVulnerabilities)

        return list[KajunSystemData]
    

    def getSystemData(self) -> list[KajunSystemData]:
        systemDataList = list[KajunSystemData]

        if self.getProgressStatus():
            return self.generateVulnerabilities(101)

        return systemDataList 

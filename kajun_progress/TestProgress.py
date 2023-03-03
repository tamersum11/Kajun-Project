import random
import socket

from PySide6.QtWidgets import QApplication

from kajun_progress.BaseKajunProgress import BaseKajunProgress
from kajun_system_info.KajunSystemData import KajunSystemData


class TestProgress(BaseKajunProgress):
    def __init__(self, app: QApplication) -> None:
        super(TestProgress, self).__init__(app)

    
    def getProgressStatus(self) -> bool:
        status = random.randint(-1, 1)
        return status == 1


    def getIpAddress(self) -> str:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    

    def getSystemDataSuccessfully(self) -> list[KajunSystemData]:
        systemDataList = []

        ip = self.getIpAddress()

        for id in range(1, 101):
            detail = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            systemDataList.append(KajunSystemData(id, ip, detail))

        return systemDataList 


    def getSystemData(self) -> list[KajunSystemData]:
        systemDataList = list[KajunSystemData]

        if self.getProgressStatus():
            return self.getSystemDataSuccessfully()

        return systemDataList 

import random
from time import sleep

from BaseProgress import BaseProgress, QApplication, KajunApplicationType

class TestProgress(BaseProgress):
    def __init__(self, app: QApplication) -> None:
        super(TestProgress, self).__init__(app)

    
    def initialise(self) -> int:
        # Splash Screen Progress
        splash = self.getKajunApplication(KajunApplicationType.SPLASHSCREEN)
        self.setKajunApplication(splash)
        self.kajunApp.setBaseProgress(self)
        self.kajunApp.show()
        
        status = self.kajunApp.startProgress()
        self.checkProgressStatus(status)
        
        return self.app.exec()
        

    def getProgressIdForCheck(self) -> int:
        return random.randint(1, 99)
    
    
    def getProgressStatus(self) -> bool:
        status = random.randint(-1, 1)
        return status == 1


    def startSplashScreenProgress(self) -> bool: 
        # progressIdForCheck = self.getProgressIdForCheck()

        for progress in range(1, 101):
            sleep(0.05)

            info = str("Lorem ipsum dolor sit amet, consectetur adipiscing elit. \n" +
                       f"Test Progress Info Label Progress Id: {progress}")
            self.infoLabel.setText(info)
            self.progressBar.setValue(progress)

            # if progress == progressIdForCheck:
            #     if not self.getProgressStatus():
            #         return False

        return True
    

    def restartSplashScreenProgress(self) -> int:
        status = self.startSplashScreenProgress()
        return self.checkProgressStatus(status)        

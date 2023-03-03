import sys
import os

from PySide6.QtWidgets import QApplication

from kajun_progress import BaseKajunProgress, TestProgress


sys.path.insert(0, os.path.dirname(__file__)) # Set Project Directory to system


def getMainProgress(app: QApplication) -> BaseKajunProgress:
    return TestProgress(app)


def main() -> int:
    app = QApplication(sys.argv)
    progress = getMainProgress(app)
    
    return progress.initialise()


if __name__ == "__main__":
    main()
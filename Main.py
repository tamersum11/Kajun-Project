import sys

from PySide6.QtWidgets import QApplication

from BaseProgress import BaseProgress
# Test Progress
from TestProgress import TestProgress


def getMainProgress(app: QApplication) -> BaseProgress:
    return TestProgress(app)


def main() -> int:
    app = QApplication(sys.argv)
    progress = getMainProgress(app)
    
    return progress.initialise()


if __name__ == "__main__":
    main()
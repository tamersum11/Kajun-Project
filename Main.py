import sys

from PySide6.QtWidgets import QApplication

from Kajun_Application import Application

def main() -> int:
    app = QApplication(sys.argv)
    widget = Application(app)
    widget.show()

    widget.startProgress()
    
    return app.exec()

if __name__ == "__main__":
    main()
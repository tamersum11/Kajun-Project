import sys

from PySide6.QtWidgets import QApplication

from KajunSplashScreen import KajunSplashScreen

def main() -> int:
    app = QApplication(sys.argv)
    splash = KajunSplashScreen(app)
    splash.show()

    splash.startProgress()
    
    return app.exec()

if __name__ == "__main__":
    main()
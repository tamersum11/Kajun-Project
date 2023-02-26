import sys

from PySide6.QtWidgets import QApplication

from KajunSplashScreen import KajunSplashScreen, DefaultInfoText, DefaultWarningText

def main() -> int:
    app = QApplication(sys.argv)
    splash = KajunSplashScreen(app)
    splash.show()

    if splash.startProgress():
        splash.showInformation(DefaultInfoText)
    else:
        splash.showWarning(DefaultWarningText)
    
    return app.exec()

if __name__ == "__main__":
    main()
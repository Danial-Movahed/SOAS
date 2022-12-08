from Gui.include import *
from Gui import Login

if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("SOAS")
    wnd = Login()
    app.exec()
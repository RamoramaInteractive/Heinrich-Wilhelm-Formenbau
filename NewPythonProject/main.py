import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from HeinrichWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainWindow()
    sys.exit(app.exec_())
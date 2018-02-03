from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QLineEdit, QSlider, QStatusBar, QProgressBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
       # self.initMenuBar()
        self.initToolbar()
        self.initStatusbar()

    def initUI(self):
        self.setWindowTitle('Heinrich Wilhelm DUI')
        self.setWindowIcon(QIcon('C:\Python\Python35-32\DLLs\hw_icon.ico'))
        self.showMaximized()

   # def initMenuBar(self):
        #Fill in

    def initToolbar(self):
        self.toolbar = self.addToolBar('MainToolbar')
        self.toolbar.setIconSize(QSize(28, 28))
        self.toolbar.setMovable(False);

        createDatabaseIcon = QAction(QIcon('C:\Python\Python35-32\DLLs\Menubar\createdatabase.png'), 'Neue Datenbank erstellen (?)', self)
        connectDatabaseIcon = QAction(QIcon('C:\Python\Python35-32\DLLs\Menubar\connectdatabase.png'), 'Datenbank verbinden (?)', self)
        deleteDatabaseIcon = QAction(QIcon('C:\Python\Python35-32\DLLs\Menubar\deletedatabase.png'), 'Datenbank löschen (?)', self)
        saveIcon  = QAction(QIcon('C:\Python\Python35-32\DLLs\Menubar\disk.png'), 'Speichern (Strg + S)', self)
        exportIcon = QAction(QIcon('C:\Python\Python35-32\DLLs\Menubar\export.png'), 'Exportieren (?)', self)
        importIcon = QAction(QIcon('C:\Python\Python35-32\DLLs\Menubar\import.png'), 'Importieren (?)', self)
        printIcon = QAction(QIcon('C:\Python\Python35-32\DLLs\Menubar\print.png'), 'Drucken (?)', self)

        undoIcon = QAction(QIcon('C:\Python\Python35-32\DLLs\Menubar\stepback.png'), 'Rückgängig (Strg + Z)', self)
        redoIcon = QAction(QIcon('C:\Python\Python35-32\DLLs\Menubar\stepforward.png'), 'Wiederholen (Strg + Y)', self)
        reloadIcon = QAction(QIcon('C:\Python\Python35-32\DLLs\Menubar\windowreload.png'), 'Aktualisieren (F5)', self)

        cutIcon = QAction(QIcon('C:\Python\Python35-32\DLLs\Menubar\scissors.png'), 'Ausschneiden (Strg + X)', self)
        copyIcon = QAction(QIcon('C:\Python\Python35-32\DLLs\Menubar\copy.png'), 'Kopieren (Strg + C)', self)
        pasteIcon = QAction(QIcon('C:\Python\Python35-32\DLLs\Menubar\paste.png'), 'Kopieren (Strg + V)', self)
        deleteIcon = QAction(QIcon('C:\Python\Python35-32\DLLs\Menubar\delete.png'), 'Löschen (Entf)', self)
        searchIcon = QAction(QIcon('C:\Python\Python35-32\DLLs\Menubar\glass.png'), 'Suchen (Strg + F)', self)

        self.toolbar.addAction(createDatabaseIcon)
        self.toolbar.addAction(connectDatabaseIcon)
        self.toolbar.addAction(deleteDatabaseIcon)
        self.toolbar.addSeparator()

        self.toolbar.addAction(saveIcon)
        self.toolbar.addAction(exportIcon)
        self.toolbar.addAction(importIcon)
        self.toolbar.addAction(printIcon)
        self.toolbar.addSeparator()

        self.toolbar.addAction(undoIcon)
        self.toolbar.addAction(redoIcon)
        self.toolbar.addAction(reloadIcon)
        self.toolbar.addSeparator()

        self.toolbar.addAction(cutIcon)
        self.toolbar.addAction(copyIcon)
        self.toolbar.addAction(pasteIcon)
        self.toolbar.addAction(deleteIcon)
        self.toolbar.addAction(searchIcon)

    def initStatusbar(self):
        self.zoomSlider = QSlider(Qt.Horizontal)
        self.zoomSlider.setMaximumWidth(200)
        self.zoomSlider.setRange(1, 200)
        self.zoomSlider.setSingleStep(10)
        self.zoomSlider.setValue(100)

        self.progressbar = QProgressBar()
        self.progressbar.setMaximumWidth(400)
        self.statusBar().addWidget(self.progressbar)
        self.statusBar().addWidget(self.zoomSlider)
        
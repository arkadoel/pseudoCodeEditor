__author__ = 'fer'

from PyQt4 import QtGui
import constantes as const
from coloreado import PseudoHighLighter

class VentanaPrincipal(QtGui.QMainWindow):

    def __init__(self):
        super(VentanaPrincipal, self).__init__(parent=None)
        self.setGeometry(100, 100, 700, 500)
        self.setWindowTitle(const.nombre_completo())

        self.iniciar_controles()
        self.maquetar()

    def iniciar_controles(self):
        self.fuente = QtGui.QFont("Courier", 12, False)
        self.editor = QtGui.QPlainTextEdit()
        self.editor.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.editor.setFont(self.fuente)


        self.iniciar_menu()

    def iniciar_menu(self):
        exitAction = QtGui.QAction(QtGui.QIcon.fromTheme('exit'), '&Salir', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Salir de la aplicacion')
        exitAction.triggered.connect(QtGui.qApp.quit)

        openAction = QtGui.QAction(QtGui.QIcon.fromTheme('new'), '&Abrir archivo', self)
        openAction.setStatusTip('Abrir un archivo para verlo')
        openAction.triggered.connect(self.showDialog)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Archivo')
        fileMenu.addAction(openAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)

    def maquetar(self):
        frame = QtGui.QFrame(parent=self)
        fondo = QtGui.QGridLayout()

        fondo.addWidget(self.editor, 0, 0)
        frame.setLayout(fondo)
        self.setCentralWidget(frame)

    def cargar_archivo(self, ruta):
        # Load syntax.py into the editor for demo purposes
        infile = open(ruta, 'r')
        self.editor.setPlainText(infile.read())


    def showDialog(self):
        dialogo = QtGui.QFileDialog(self)
        dialogo.setWindowTitle('Abrir archivo')
        #dialogo.setNameFilter('Images (*.png *.xpm *.jpg)')
        dialogo.setFileMode(QtGui.QFileDialog.ExistingFile)
        dialogo.setDirectory('/home')


        if dialogo.exec_() == QtGui.QDialog.Accepted:
            fname = dialogo.selectedFiles()[0]
            self.cargar_archivo(fname)
            dialogo.saveState()
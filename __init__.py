from coloreado import PseudoHighLighter

__author__ = 'fer'
__version__ = '0.0.1'

from PyQt4 import QtGui
import sys
from ventanas.principal import VentanaPrincipal

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    v = VentanaPrincipal()
    v.show()

    colorear = PseudoHighLighter(v.editor.document())
    v.editor.update()

    sys.exit(app.exec_())


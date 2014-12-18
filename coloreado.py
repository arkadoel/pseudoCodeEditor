from PyQt4.QtCore import QRegExp
from PyQt4.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter
import constantes as const

def formatear(color, style=''):
    """
    Devuelve QTextCharFormat con los atributos dados
    """
    qcolor = QColor()
    qcolor.setNamedColor(color)

    formato = QTextCharFormat()
    formato.setForeground(qcolor)
    if 'bold' in style:
        formato.setFontWeight(QFont.Bold)
    if 'italic' in style:
        formato.setFontItalic(True)

    return formato


# Syntax styles that can be shared by all languages
ESTILOS = {
    'palabra': formatear('blue'),
    'operador': formatear('gray'),
    'corchetes': formatear('DarkGray', 'bold'),
    'libreria': formatear('purple', 'italic'),
    'cadena': formatear('red'),
    'cadena2': formatear('darkMagenta'),
    'commentario': formatear('darkGreen', 'italic'),
    'numberos': formatear('brown'),
    'tipos': formatear('DarkRed', 'italic'),
    'INICIO': formatear('Red', 'bold'),
}

class PseudoHighLighter(QSyntaxHighlighter):

    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)

        self.tri_single = (QRegExp("'''"), 2, ESTILOS['cadena2'])
        self.tri_double = (QRegExp('"""'), 2, ESTILOS['cadena2'])

        reglas = []

        # Keyword, operator, and brace rules
        reglas += [(r'\b%s\b' % w, 0, ESTILOS['palabra'])
            for w in const.PALABRAS]
        reglas += [(r'%s' % o, 0, ESTILOS['operador'])
            for o in const.OPERADORES]
        reglas += [(r'%s' % b, 0, ESTILOS['corchetes'])
            for b in const.CORCHETES]
        reglas += [(r'%s' % b, 0, ESTILOS['tipos'])
            for b in const.TIPOS]

        # All other rules
        reglas += [

            (r'\bINICIO\b', 0, ESTILOS['INICIO']),

            # Double-quoted string, possibly containing escape sequences
            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, ESTILOS['cadena']),
            # Single-quoted string, possibly containing escape sequences
            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, ESTILOS['cadena']),

            # From '#' until a newline
            (r'#[^\n]*', 0, ESTILOS['libreria']),
            (r'//[^\n]*', 0, ESTILOS['commentario']),

            # Numeric literals
            (r'\b[+-]?[0-9]+[lL]?\b', 0, ESTILOS['numberos']),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, ESTILOS['numberos']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, ESTILOS['numberos']),
        ]

        # Build a QRegExp for each pattern
        self.reglas = [(QRegExp(pat), index, fmt)
            for (pat, index, fmt) in reglas]

    def highlightBlock(self, text):
        """Apply syntax highlighting to the given block of text.
        """
        # Do other syntax formatting
        for expression, nth, format in self.reglas:
            index = expression.indexIn(text, 0)

            while index >= 0:
                # We actually want the index of the nth match
                index = expression.pos(nth)
                length = expression.cap(nth).__len__()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        # Do multi-line strings
        in_multiline = self.match_multiline(text, *self.tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *self.tri_double)


    def match_multiline(self, text, delimiter, in_state, style):
        """Do highlighting of multi-line strings. ``delimiter`` should be a
        ``QRegExp`` for triple-single-quotes or triple-double-quotes, and
        ``in_state`` should be a unique integer to represent the corresponding
        state changes when inside those strings. Returns True if we're still
        inside a multi-line string when this function is finished.
        """
        # If inside triple-single quotes, start at 0
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        # Otherwise, look for the delimiter on this line
        else:
            start = delimiter.indexIn(text)
            # Move past this match
            add = delimiter.matchedLength()

        # As long as there's a delimiter match on this line...
        while start >= 0:
            # Look for the ending delimiter
            end = delimiter.indexIn(text, start + add)
            # Ending delimiter on this line?
            if end >= add:
                length = end - start + add + delimiter.matchedLength()
                self.setCurrentBlockState(0)
            # No; multi-line string
            else:
                self.setCurrentBlockState(in_state)
                length = text.__len__() - start + add
            # Apply formatting
            self.setFormat(start, length, style)
            # Look for the next match
            start = delimiter.indexIn(text, start + length)

        # Return True if still inside a multi-line string, False otherwise
        if self.currentBlockState() == in_state:
            return True
        else:
            return False


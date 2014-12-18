__author__ = 'fer'

APP_NAME = 'Pseudo Code Editor'
APP_VERSION = '0.0.1'

def nombre_completo():
    """
    Devuelve el nombre de la aplicacion completo
    :return:
    """
    return APP_NAME + ' ' + APP_VERSION

#Palabras reservadas en PseudoCodigo
PALABRAS = [
    'Y', 'O', 'Usar', 'Verdadero', 'Falso', 'EspacioDeNombres',
    'Clase', 'Enumeracion', 'Estructura', 'Retorno',
    'Entonces', 'Fin', 'FinSi', 'FinMientras', 'FinClase',
    'FinFuncion', 'FinProcedimiento', 'FinEstructura', 'FinPara',
    'No', 'Repetir', 'HastaQue', 'Mientras', 'Si', 'Sino', 'Para',
    'SegunSea', 'Caso', 'PorDefecto', 'Rompe', 'Saltar_a',
    'Publico', 'Privado', 'Protegido', 'Amigo', 'Externo',
    'Estatico', 'Procedimiento', 'Nuevo', 'Aqui', 'Intentar',
    'Capturar', 'Finalmente', 'Excepcion','Hacer', 'Contiene',
]

TIPOS = [
    'Entero', 'Frase', 'Real', 'EnteroCorto', 'EnteroLargo', 'Caracter', 'Booleano',
    'RealLargo', 'Constante',
]

# Operadores
OPERADORES = [
    '=',
    # Comparacion
    '==', '!=', '<', '<=', '>', '>=',
    # Aritmeticos
    '\+', '-', '\*', '/', '//', '\%', '\*\*',
    # Asignacion y operacion
    '\+=', '-=', '\*=', '/=', '\%=',
    # Binarios
    '\^', '\|', '\&', '\~', '>>', '<<', '::', ';', ',',

]

# Otros operadores
CORCHETES = [
    '\{', '\}', '\(', '\)', '\[', '\]',
]
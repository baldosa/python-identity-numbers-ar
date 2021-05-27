import re

def clean(dni):
    """
    Saca todos los caracteres no numericos del valor
    """
    dni = str(dni)
    return re.sub("[^0-9]", "", dni)


def dot_format(dni):
    """
    Formatea el numero en xx.xxx.xxx
    """
    dni = str(dni)
    try:
        is_valid(dni)
        if len(dni) == 7:
            return f'{dni[0:1]}.{dni[1:4]}.{dni[-3]}'
        else:
            return f'{dni[0:2]}.{dni[2:5]}.{dni[-3:]}'
    except Exception as e:
        print(e)

def is_valid(dni):
    """
    Valida que el número parezca un DNI válido
    """
    dni = str(dni)
    
    if len(dni) not in [7, 8]:
        raise Exception('Cantidad incorrecta de caracteres')

    if len(re.sub("[0-9]", "", dni)) > 0:
        raise Exception('Hay caracteres no numéricos')

    return True
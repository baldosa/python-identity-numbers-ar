"""
El CUIL (Código Único de Identificación Laboral) o CUIT
(Código Único de Identificación Tributaria) sirve para identificar
a las personas de manera única en la República Argentina.
Mas info:
* https://es.wikipedia.org/wiki/Clave_Única_de_Identificación_Tributaria
* https://es.wikipedia.org/wiki/C%C3%B3digo_%C3%9Anico_de_Identificaci%C3%B3n_Laboral


"""
import re

cuil_starts = [ '20', '23', '24', '27', '30', '33' ]

def clean(cuil):
    """
    Saca todos los caracteres no numericos del valor
    """
    cuil = str(cuil)
    return re.sub("[^0-9]", "", cuil)

def check_digit(cuil):
    """
    Valida dígito verificador de un cuil "limpio" previo check
    """
    cuil = str(cuil)
    digitos = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    check = sum(d * int(c) for d, c in zip(digitos, cuil)) % 11

    if (cuil[-1] == '012345678990'[11 - check]):
        return True
    else:
        return False

def score_format(cuil):
    """
    Formatea el numero en xx-xxxxxxx-x de un cuil "limpio" previo check
    """
    cuil = str(cuil)
    try:
        is_valid(cuil)
        return f'{cuil[0:2]}-{cuil[2:10]}-{cuil[-1]}'
    except Exception as e:
        print(e)
    
def is_valid(cuil):
    """
    Valida que el número parezca un CUIL válido
    """
    cuil = str(cuil)
    
    if len(cuil) != 11:
        raise Exception('Cantidad incorrecta de caracteres')

    if len(re.sub("[0-9]", "", cuil)) > 0:
        raise Exception('Hay caracteres no numéricos')

    if not check_digit(cuil):
        raise Exception('Dígito verificador inválido')

    if cuil[0:2] not in cuil_starts:
        raise Exception('Los números iniciales son incorrectos')

    return True

def gen_dni(cuil):
    """Devuelve el DNI de un CUIL "válido"
    """
    cuil = str(cuil)
    try:
        is_valid(cuil)
        return cuil[2:10]
    except Exception as e:
        print(e)

    


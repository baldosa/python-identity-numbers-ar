from identitynumbersar import cuil 


def test_cuil():
    cuil_valido = '24345399018'
    cuil_invalido = '241145399011'
    cuil_invalido_digito_verificador = '24345399016'

    assert cuil.clean(cuil_valido) == '24345399018'
    assert cuil.check_digit(cuil_invalido_digito_verificador) == False
    assert cuil.check_digit(cuil_valido) == True
    assert cuil.score_format(cuil_valido) == '24-34539901-8'
    assert cuil.is_valid(cuil_valido) == True
    
    try:
        cuil.is_valid(cuil_invalido)
        assert False
    except:
        assert True
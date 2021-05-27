# python-identity-numbers-ar
Mini librería para limpiar/formatear o validar CUIL/T y DNI Argentinos con Python >=3.8
## Uso
### CUIL/T
```
from identitynumbersar import cuil
c = '24345399018'
print(cuil.clean(f'{c}asdqweasuiklasd'))
>>24345399018
print(cuil.check_digit(c))
True
print(cuil.score_format(c))
'24-34539901-8'
print(cuil.is_valid(c))
True
print(cuil.gen_dni(c))
34539901
```

### DNI
```
from identitynumbersar import dni
d = '34539901'
print(dni.clean(f'{c}asdqweasuiklasd'))
>>34539901
print(dni.dot_format(c))
'34.539.901'
print(dni.is_valid(c))
True
```

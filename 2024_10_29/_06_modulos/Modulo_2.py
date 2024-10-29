import _06_modulos.Modulo_1
from api import Inputs

print(_06_modulos.Modulo_1.PROVINCIA)

valor = Inputs.read_int()
incremento = _06_modulos.Modulo_1.inc(valor)
print(incremento)


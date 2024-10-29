# -------------------------------------------------------------
# Información sobre el módulo
# -------------------------------------------------------------
print(dir())
print(__file__)
print(__name__)
print(__package__)
print(__doc__)

print('-' * 80)

# -------------------------------------------------------------
# Ejemplos mostrar información sobre otros módulos
# -------------------------------------------------------------
import sys
from api import Data

print(dir(Data))

print(dir(sys))

print(dir(sys.path))

__variable_privada = 89

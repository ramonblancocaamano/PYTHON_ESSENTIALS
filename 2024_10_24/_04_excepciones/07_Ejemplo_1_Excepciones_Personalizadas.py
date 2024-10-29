class OtraVezConElMismoNumeroTresError(ArithmeticError):
    __mensaje = 'Error de tipo OtraVezConElMismoError'
    def __init__(self, msg=None):
        msg = msg if msg else OtraVezConElMismoNumeroTresError.__mensaje
        ArithmeticError.__init__(self, msg)

class PersonalError(Exception):
    def __init__(self, message='El número no puede ser 13'):
        Exception.__init__(self, message)


class SubclassError(PersonalError):
    def __init__(self, message=''):
        PersonalError._init__(self, message)


n = int(input('Número => '))
if n == 3:
    raise OtraVezConElMismoNumeroTresError


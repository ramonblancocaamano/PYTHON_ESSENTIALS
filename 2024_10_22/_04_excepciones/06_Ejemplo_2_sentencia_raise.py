def bad_fun(n):
    # Abrir la base de datos
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        # Cerrar la base de datos
        raise  # Esto es equivalente al throw de Java, C#


try:
    bad_fun(0)
except ArithmeticError:
    print("¡Ya veo!")

print("FIN.")

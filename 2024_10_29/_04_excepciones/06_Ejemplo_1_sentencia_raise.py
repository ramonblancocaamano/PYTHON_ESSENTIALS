def bad_fun(n):
    t = input('Cualquier cosa')
    print(t)
    raise


try:
    bad_fun(4523)
except ArithmeticError as mensaje:
    print("¿Que pasó? ¿Un error?", mensaje)

print("FIN.")


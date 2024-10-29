from os import strerror


def escribir_lineas(nombre, numero=20):
    try:
        with open(nombre, 'w+') as f:
            for n in range(numero):
                f.write(f"test {n + 1}\n")
            f.seek(0)
            lines = f.read()
            print(lines)
    except IOError as e:
        print(strerror(e.errno))

escribir_lineas('c:/datasets/data/lineas.txt')

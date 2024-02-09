def es_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    else:
        for i in range(3, int(numero**0.5) + 1, 2):
            if numero % i == 0:
                return False
        return True

# Casos de prueba
def test_es_primo():
    # Prueba de números primos
    if es_primo(2):
        print("Prueba de número primo pasada con éxito.")
    else:
        print("Error en la prueba de número primo.")

    if es_primo(7):
        print("Prueba de número primo pasada con éxito.")
    else:
        print("Error en la prueba de número primo.")

    # Prueba de números no primos
    if not es_primo(1):
        print("Prueba de número no primo pasada con éxito.")
    else:
        print("Error en la prueba de número no primo.")

    if not es_primo(9):
        print("Prueba de número no primo pasada con éxito.")
    else:
        print("Error en la prueba de número no primo.")

    # Prueba de número grande
    if es_primo(104729):
        print("Prueba de número primo grande pasada con éxito.")
    else:
        print("Error en la prueba de número primo grande.")

    print("Todos los casos de prueba han sido ejecutados.")

# Ejecutar los casos de prueba
test_es_primo()
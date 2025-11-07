import random

# Simula la caída de canicas
def simular_canicas(n_canicas=3000, n_niveles=12):
    contenedores = [0] * (n_niveles + 1)

    for _ in range(n_canicas):
        posicion = 0

        for _ in range(n_niveles):
            direccion = random.choice(["izquierda", "derecha"])
            if direccion == "derecha":
                posicion += 1

        contenedores[posicion] += 1

    return contenedores

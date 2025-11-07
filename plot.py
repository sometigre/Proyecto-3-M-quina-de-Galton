import matplotlib.pyplot as plt

# Dibuja el histograma
def mostrar_histograma(lista_contenedores):
    numeros_contenedores = list(range(len(lista_contenedores)))
    plt.bar(numeros_contenedores, lista_contenedores)
    plt.xlabel("Número del contenedor")
    plt.ylabel("Cantidad de canicas")
    plt.title("Resultado de la simulación de las canicas")
    plt.show()

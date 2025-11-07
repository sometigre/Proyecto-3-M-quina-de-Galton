from galton import simular_canicas
from plot import mostrar_histograma

def main():
    print("Bienvenido a la simulación de la máquina de Galton")

    canicas = 3000
    niveles = 12

    resultado = simular_canicas(canicas, niveles)

    print("Resultado final de las canicas en los contenedores:")
    print(resultado)

    mostrar_histograma(resultado)

main()

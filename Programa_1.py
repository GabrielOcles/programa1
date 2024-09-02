# busqueda_matriz.py

def buscar_valor(matriz, valor):
    """
    Busca un valor en una matriz bidimensional.

    :param matriz: Lista de listas (matriz) donde se realizará la búsqueda.
    :param valor: Valor que se busca en la matriz.
    :return: Una tupla con la fila y la columna del valor si se encuentra, None en caso contrario.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Devuelve la posición (fila, columna)
    return None


def main():
    # Definimos una matriz de 3x3
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Valor a buscar
    valor_a_buscar = 5

    # Llamamos a la función de búsqueda
    resultado = buscar_valor(matriz, valor_a_buscar)

    # Mostramos el resultado
    if resultado:
        print(f"Valor {valor_a_buscar} encontrado en la posición: {resultado}")
    else:
        print(f"Valor {valor_a_buscar} no encontrado en la matriz.")


# Ejecutamos la función principal
if __name__ == "__main__":
    main()
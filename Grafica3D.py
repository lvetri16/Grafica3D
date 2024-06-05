import numpy as np
from numpy.linalg import inv

def iteracion_potencia_inversa(matriz_A, num_iteraciones: int):
    vector_b_k = np.random.rand(matriz_A.shape[1])
    matriz_A_inversa = inv(matriz_A)
    lista_vector_b_k = [vector_b_k]
    for _ in range(num_iteraciones):
        vector_b_k1 = np.dot(matriz_A_inversa, vector_b_k)
        norma_vector_b_k1 = np.linalg.norm(vector_b_k1)
        vector_b_k = vector_b_k1 / norma_vector_b_k1
        lista_vector_b_k.append(vector_b_k)
    return lista_vector_b_k
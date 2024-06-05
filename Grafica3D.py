import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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

matriz_A = np.array([[0.5, 0.5], [0.2, 0.8]])
lista_vector_b_k = iteracion_potencia_inversa(matriz_A, 10)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i, vector_b_k in enumerate(lista_vector_b_k):
    ax.scatter(vector_b_k[0], vector_b_k[1], i)

ax.set_xlabel('Componente 1')
ax.set_ylabel('Componente 2')
ax.set_zlabel('Iteración')
plt.title('Evolución del vector b_k en el método de la potencia inversa')
plt.show()
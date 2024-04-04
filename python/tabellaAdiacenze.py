import networkx as nx
import matplotlib.pyplot as plt # libreria pe grafici
import numpy as np

def prettyPrint(matrice, separatore = " "):
    for riga in matrice:
        rigaStr=[str(x) for x in riga]
        print(separatore.join(rigaStr))
        
def dizToMat():
    dizR = {0:[2,3], 1:[2,4], 2:[0,1,3], 3:[0,2,4], 4:[1,3]}
    n  = len(dizR)
    mat= [[0]*n for _ in range (n)]
    for k, v in dizR.items():
        for  h in v:
            mat[k][h] = 1      
    prettyPrint(mat)
    return mat

def matToDiz(mat):
    return {i: [j for j,n in enumerate(mat[i]) if n != 0] for i in range(len(mat))}

def main():
    matToDiz(dizToMat())
    disegnaMat(dizToMat())

def disegnaMat(matrice_adiacenza):
    # Creare un grafo da un array di adiacenza
    grafo = nx.Graph(np.array(matrice_adiacenza))

    # Disegnare il grafo
    posizioni = nx.spring_layout(grafo)  # Posizioni dei nodi
    nx.draw(grafo, pos=posizioni, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)

    # Mostrare il grafico
    plt.show()


if __name__ == '__main__':
    main()
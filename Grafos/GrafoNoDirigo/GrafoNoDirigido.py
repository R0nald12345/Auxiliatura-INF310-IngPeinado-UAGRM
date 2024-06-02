from ListaSimple import ClaseLista
from collections import deque  # Importar deque para usar como cola en BFS


class GrafoNoDirigido:
    
    
    MAXVERTICE = 49

    def __init__(self):
        self.vectorVertice = [None] * (self.MAXVERTICE + 1)
        self.vectorMarcado = [False] * (self.MAXVERTICE + 1)
        self.n = -1 #cantidad de Vertice

    def add(self):
        if self.n == self.MAXVERTICE:
            print("Capacidad al Límite")
            return
        else:
            self.n += 1
            self.vectorVertice[self.n] = ClaseLista()
            
    def cantidadVertice(self):
        return self.n + 1

    def isVerticeValido(self, v):
        return 0 <= v <= self.n

    def addArista(self, u, v):
        if not self.isVerticeValido(u) or not self.isVerticeValido(v):
            return
        self.vectorVertice[u].add(v)
        self.vectorVertice[v].add(u)

    def printListas(self):
        if self.cantidadVertice() == 0:
            print("{Grafo Vacío}")
        else:
            for i in range(self.n + 1):
                print(f"V[{i}]-->| {self.vectorVertice[i].mostrar_lista()} |")

    # def esLinea(self):
    #     self.desmarcarTodos()
    #     cola = []

    #     for nodo in range(self.n + 1):
    #         if not self.isMarcado(nodo) and self.vectorVertice[nodo].length() == 2:
    #             cola.append(nodo)
    #             self.marcar(nodo)
    #             numAristas = 0
    #             while cola:
    #                 actual = cola.pop(0)
    #                 numAristas += 1
    #                 for j in range(self.vectorVertice[actual].length()):
    #                     vecino = self.vectorVertice[actual].get(j)
    #                     if not self.isMarcado(vecino):
    #                         cola.append(vecino)
    #                         self.marcar(vecino)
    #             if numAristas == 1:
    #                 return True
    #     return False

    # def isLineal(self):
    #     self.desmarcarTodos()
    #     contador = 0
    #     for i in range(self.n + 1):
    #         self.marcar(i)
    #         for datoL in self.vectorVertice[i].mostrar_lista():
    #             if not self.isMarcado(datoL):
    #                 contador += 1
    #                 self.marcar(datoL)
    #             if contador > 1:
    #                 return False
    #         contador = 0
    #     return True

    def desmarcarTodos(self):
        self.vectorMarcado = [False] * (self.MAXVERTICE + 1)

    def marcar(self, u):
        self.vectorMarcado[u] = True

    def isMarcado(self, u):
        return self.vectorMarcado[u]

    # DFS iterativo utilizando una pila
    def DFS(self, start):
        self.desmarcarTodos()  # Desmarcar todos los vértices
        stack = [start]  # Inicializar la pila con el vértice de inicio
        while stack:
            current = stack.pop()  # Obtener el vértice actual de la pila
            if not self.isMarcado(current):  # Si el vértice no está marcado
                self.marcar(current)  # Marcar el vértice como visitado
                print(current, end=' ')  # Imprimir el vértice visitado
                # Agregar los vértices adyacentes no marcados a la pila
                for neighbor in self.vectorVertice[current].mostrar_lista():
                    if not self.isMarcado(neighbor):
                        stack.append(neighbor)



    # BFS iterativo utilizando una cola
    def BFS(self, start):
        self.desmarcarTodos()  # Desmarcar todos los vértices
        queue = deque([start])  # Inicializar la cola con el vértice de inicio
        while queue:
            current = queue.popleft()  # Obtener el vértice actual de la cola
            if not self.isMarcado(current):  # Si el vértice no está marcado
                self.marcar(current)  # Marcar el vértice como visitado
                print(current, end=' ')  # Imprimir el vértice visitado
                # Agregar los vértices adyacentes no marcados a la cola
                for neighbor in self.vectorVertice[current].mostrar_lista():
                    if not self.isMarcado(neighbor):
                        queue.append(neighbor)


      # Generar matriz de adyacencia
    def matrizAdyacencia(self):
        matriz = [[0] * (self.n + 1) for _ in range(self.n + 1)]  # Inicializar matriz de adyacencia con ceros
        for i in range(self.n + 1):
            for j in self.vectorVertice[i].mostrar_lista():
                matriz[i][j] = 1  # Si hay adyacencia, poner 1 en la matriz
        return matriz

    def mostrarMatrizAdyacencia(self):
        cantF = self.cantidadVertice()
        cantC = self.cantidadVertice()
        matriz = [[0] * cantC for _ in range(cantF)]
        for fil in range(cantF):
            adyacentes = self.vectorVertice[fil].mostrar_lista()
            for ady in adyacentes:
                matriz[fil][ady] = 1
        for fila in matriz:
            print("[" + "][".join(map(str, fila)) + "]")
                    
      

if __name__ == "__main__":
    gn1 = GrafoNoDirigido()
    gn1.add()
    gn1.add()
    gn1.add()
    gn1.add()
    # gn1.add()
    # gn1.add()
    # gn1.add()
    
    gn1.addArista(0, 2)
    gn1.addArista(2, 1)
    
    gn1.addArista(1, 1)
    gn1.addArista(1, 3)
    
    
    
    # gn1.addArista(3, 5)
    # gn1.addArista(3, 6)
    
    gn1.printListas()
    print()
    print(gn1.mostrarMatrizAdyacencia())
    # print(gn1.isLineal())
    # print('Recorrido en BFS')
    # gn1.BFS(0)
    # # print('')
    # # print('Recorrido en DFS')
    # # gn1.BFS(0)
    # gn1.matrizAdyacencia()
class Grafo:
    
    def __init__(self, nro_de_vertice_inicial=0):
        if nro_de_vertice_inicial < 0:
            raise ValueError("Error: número de vértices inicial no válido")
        self.lista_de_adyacencia = []
        self.cant_aristas = 0
        for _ in range(nro_de_vertice_inicial):
            self.lista_de_adyacencia.append([])

    def insertar_vertice(self):
        self.lista_de_adyacencia.append([])

    def cantidad_de_aristas(self):
        return self.cant_aristas

    def cantidad_de_vertices(self):
        return len(self.lista_de_adyacencia)

    def validar_vertice(self, posicion_de_vertice):
        if posicion_de_vertice < 0 or posicion_de_vertice >= self.cantidad_de_vertices():
            raise ValueError(f"El Vértice {posicion_de_vertice} no pertenece al grafo")


    def insertar_arista(self, pos_vertice_origen, pos_vertice_destino):
        self.validar_vertice(pos_vertice_origen)
        self.validar_vertice(pos_vertice_destino)
        if self.existe_adyacencia(pos_vertice_origen, pos_vertice_destino):
            raise ValueError("Ya existe adyacencia")
        self.cant_aristas += 1
        self.lista_de_adyacencia[pos_vertice_origen].append(pos_vertice_destino)
        if pos_vertice_origen == pos_vertice_destino:
            self.lista_de_adyacencia[pos_vertice_origen].append(pos_vertice_origen)


    def existe_adyacencia(self, pos_vertice_origen, pos_vertice_destino):
        self.validar_vertice(pos_vertice_origen)
        self.validar_vertice(pos_vertice_destino)
        adyacencia_del_origen = self.lista_de_adyacencia[pos_vertice_origen]
        return pos_vertice_destino in adyacencia_del_origen



    def mostrar_grafo_no_dirigido(self):
        for i in range(len(self.lista_de_adyacencia)):
            vertice = f"[{i}]"
            adyacentes = "["
            for j in self.lista_de_adyacencia[i]:
                adyacentes += f"{j},"
            if self.lista_de_adyacencia[i]:
                adyacentes = adyacentes[:-1]  # Eliminar la última coma
            adyacentes += "]"
            print(f"{vertice} -> {adyacentes}")
            
            

if __name__ == "__main__":
    grafo_no_dirigido = Grafo()
    grafo_no_dirigido.insertar_vertice()
    grafo_no_dirigido.insertar_vertice()
    grafo_no_dirigido.insertar_vertice()
    grafo_no_dirigido.insertar_vertice()
    grafo_no_dirigido.insertar_vertice()

    grafo_no_dirigido.insertar_arista(0, 1)
    grafo_no_dirigido.insertar_arista(0, 2)
    grafo_no_dirigido.insertar_arista(0, 3)
    grafo_no_dirigido.insertar_arista(1, 0)
    grafo_no_dirigido.insertar_arista(1, 1)
    grafo_no_dirigido.insertar_arista(2, 0)
    grafo_no_dirigido.insertar_arista(3, 0)
    
    grafo_no_dirigido.mostrar_grafo_no_dirigido()

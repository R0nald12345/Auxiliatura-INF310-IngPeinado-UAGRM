from ClaseNodo import Nodo

class Arbol:
    __raiz__ = None # Puntero 
    __n__ = 0 #Cantidad de Nodos

    #Contructor
    def __init__(self):
        self.__raiz__ = None
        self.__n__ = 0;


    #x = valor (100)
    def insertar(self, x):
        self.__raiz__ = self.__insertarMask(self.__raiz__, x)


    #Funcion (Me retorna el nuevo Arbol)
    def __insertarMask(self, nodoRaiz, x):
        if nodoRaiz is None: 
            return Nodo(x)
        else:
            if(x < nodoRaiz.getData()):
                nodoRaiz.__hijoIzquierdo__ = self.__insertarMask(nodoRaiz.getHijoIzquierdo(),x)
            else:
                nodoRaiz.__hijoDerecho__ = self.__insertarMask(nodoRaiz.getHijoDerecho(),x)
        
        


    def inOrden(self):
        if self.__raiz__ is None:
            print("El arbol esta Vacio")
        else:
            self.__inOrdenMask(self.__raiz__)
        print("---------------------------------------")

    def __inOrdenMask(self, nodo):
        if nodo is not None:
            self.__inOrdenMask(nodo.getHijoIzquierdo()) # Izquierdo
            print(nodo.getData())       #Padre
            self.__inOrdenMask(nodo.getHijoDerecho()) #Derecho



    def preOrden(self):
        if self.__raiz__ is None:
            print("El arbol esta Vacio")
        else:
            self.__preOrdenMask(self.__raiz__)


    def __preOrdenMask(self, nodo):  #Padre, Izquierdo, Derecho
        if nodo is not None:
            print(nodo.getData())  # Padre
            self.__inOrdenMask(nodo.getHijoIzquierdo())  # Izquierdo
            self.__inOrdenMask(nodo.getHijoDerecho())  # Derecho


    #Post ORden = Izuiqerdo Derecho, Padre

    #Verificar Arbol Vacio
    def isVacio(self):
        if self.__raiz__ is None:
            print("El arbol esta vacio")
        else:
            print("El arbol no esta vacio")


    def isHoja(self, nodo):
        if(nodo.getHijoIzquierdo()is None  and Nodo.getHijoDerecho is None):
            print("El nodo es Hoja")
        else:
            print("El nodo no es hoja")


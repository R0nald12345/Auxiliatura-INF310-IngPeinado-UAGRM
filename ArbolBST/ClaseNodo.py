class Nodo:
    __data__ = 0 
    __hijoIzquierdo__ = None
    __hijoDerecho__ = None

    #Constructor 
    def __init__(self, data):
        self.__hijoDerecho__ = None
        self.__hijoIzquierdo__ = None
        self.__data__ = data

    #Getters and Setters
    def getData(self):
        return self.__data__

    def setData(self,data):
        self.__data__ = data

    def getHijoIzquierdo(self):
        return self.__hijoIzquierdo__

    def setHijoIzquierdo(self, hijoIzquierdo):
        self.__hijoIzquierdo__ = hijoIzquierdo

    def getHijoDerecho(self):
        return self.__hijoDerecho__

    def setHijoDerecho(self, hijoDerecho):
        self.__hijoDerecho__ = hijoDerecho


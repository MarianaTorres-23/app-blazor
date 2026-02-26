class pilaEstatica:
    def __init__(self,capacidad):
        #inicializa una lista de tamaño fijo con valores nulos 
        self.capacidad = capacidad
        self.elementos = [None] * capacidad
        self.cima = -1
    def vacia(self):
        return self.cima == -1
    def llena(self):
        return self.cima == self.capacidad - 1
    def push(self,elemento):
        if not self.llena():
         self.cima += 1
         self.elementos[self.cima] = elemento
        else:
            print("La pila está llena. No se puede agregar el elemento.")   
    def pop(self):
        if not self.vacia():
            elemento = self.elementos[self.cima]
            self.elementos[self.cima] = None  # Limpiar el valor para evitar referencias innecesarias
            self.cima -= 1
            return elemento
        else:
            print("La pila está vacía. No se puede eliminar ningún elemento.")
    def top(self):
        if not self.vacia():
            return self.elementos[self.cima]
        else:
            print("La pila está vacía. No hay elemento en la cima.")
    def __str__(self):
        salida = ""
        if not self.vacia():
            for i in range(self.cima, -1, -1):
                if i == self.cima:
                    salida += str(self.elementos[i]) + " <- cima\n"
                else:
                    salida += str(self.elementos[i]) + "\n"
        else:
            salida = "La pila está vacía."
        return salida
    #programa principal
pila = pilaEstatica(5)
print ("push 1")
pila.push(1)
print ("push 2")    
pila.push(2)
print ("push 3") 
pila.push(3)
print("\npila:\n",pila, sep="" )
print ("cima de la pila", pila.pop())
elemento_eliminado = pila.pop()
print("Elemento eliminado:", elemento_eliminado)
print("\npila:\n",pila, sep="" )
    
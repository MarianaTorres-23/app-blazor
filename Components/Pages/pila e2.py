class pilaEstatica:
    def __init__(self,capacidad):
        #inicializa una lista de tamaño fijo con valores nulos 
        self.capacidad = capacidad
        self.elementos = [None] * capacidad
        self.cima = -1
        self.error = 0 
    def vacia(self):
        return self.cima == -1
    def llena(self):
        return self.cima == self.capacidad - 1
    def push(self, valor_agregar):
        if not self.llena():
         self.cima += 1
         self.elementos[self.cima] = valor_agregar
        else:
            self.error = 1
    def pop(self):
        if not self.vacia():
            valor_leido = self.elementos[self.cima]
            self.elementos[self.cima] = None  # Limpiar el valor para evitar referencias innecesarias
            self.cima -= 1
            return valor_leido
        else:
            self.error = 2 
    def top(self):
        if not self.vacia():
            return self.elementos[self.cima]
        else:
            self.error = 3
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
def mensaje(error):
    if error == 0:
        msg = "parentesis balanceados"
    elif error == 1:
        msg = "pila llena"
    elif error == 2:
        msg = "existen mas parentesis derechos que izquierdos"
    elif error == 3:        
        msg = "existen mas parentesis izquierdos que derechos"
    else: 
        msg = "error desconocido"
    print(msg)
pila = pilaEstatica(10)
expresion = input ("ingresa una expresion valida:")
i = 0
while i <len(expresion) and pila.error == 0:
    if expresion [i] == "(":
        pila.push(expresion[i])
    elif expresion [i] == ")":
        pila.pop()
    i += 1
if not pila.vacia () and pila.error == 0:
    mensaje(3)
else:    
    mensaje(pila.error)
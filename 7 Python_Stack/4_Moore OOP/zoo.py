class Animal(object):
    def __init__(self):
        self.nombre = input("ingrese el nombre")
        self.edad = input("ingrese su edad")
        self.salud = 50
        self.felicidad = 50
    
    def alimentar(self, alimentado):
        if alimentado == True:
            self.felicidad += 10
            self.salud += 10
        else:
            self.salud -= 10 
            self.felicidad -= 10
        return self
    
    def caminar(self):
        self.salud -= 5
        self.felicidad += 10
        return self

    def jugar(self):
        self.salud -= 5
        self.felicidad += 10
        return self
    
    def display_info(self):
        print ("***Info Animal***")
        print ("Nombre: " + str(self.nombre))
        print ("Edad: ", self.edad)
        print ("Salud: " + str(self.salud))
        print ("Felicidad: " + str(self.felicidad))
        #return self

# Crea un nuevo animal
# animal1 = Animal("Fresia",15, 50, 75) 
# animal1.alimentar(True).alimentar(True).caminar().jugar().display_info()

class Aguila(Animal):
    def __init__(self):
        super().__init__()
        self.salud = 75
        self.felicidad = 75
        self.tipo = "Ave"
        
    def volar(self):
        self.salud -= 5
        self.felicidad += 5
        return self
    
    def alimentar(self, alimentado):
        if alimentado == True:
            self.felicidad += 15
            self.salud += 25
        else:
            self.salud -= 25 
            self.felicidad -= 15
        return self

#animal2 = Aguila()
#animal2.alimentar(True).volar().display_info()

class Chita(Animal):
    def __init__(self):
        super().__init__()
        self.salud = 60
        self.felicidad = 70
        self.tipo = "Felino"
        
    def correr(self):
        self.salud -= 10
        self.felicidad += 5
        return self
    
    def alimentar(self, alimentado):
        if alimentado == True:
            self.felicidad += 18
            self.salud += 28
        else:
            self.salud -= 28
            self.felicidad -= 18
        return self
    
    def caminar(self):
        super().caminar()

    def jugar(self):
        super().jugar()

class OsoPolar(Animal):
    def __init__(self):
        super().__init__()
        self.salud = 70
        self.felicidad = 65
        self.tipo = "Oso"
        
    def nadar(self):
        self.salud -= 5
        self.felicidad += 5
        return self   
    
    def alimentar(self, alimentado):
        if alimentado == True:
            self.felicidad += 20
            self.salud += 30
        else:
            self.salud -= 20 
            self.felicidad -= 10
        return self
    
    def caminar(self):
        super().caminar()

    def jugar(self):
        super().jugar()
    
class Zoo:
    def __init__(self, zoologico):
        self.animales = []
        self.nombre = zoologico
        
    def add_animal(self, tipo, nombre):
        self.animales.append(tipo(nombre))
    
    def print_all_info(self):
        print("-"*10, self.nombre, "-"*10)
        for animal in self.animales:
            animal.display_info()
        return self
    
    def alimentarAll(self):
        print("*"*18, self.nombre, "*"*18)
        print("*"*18, "Alimentando", "*"*18)
        for a in range(0, len(self.animales)):
            self.animales[a].alimentar()
    
    def addmasivo(self):
        a = ""
        while a.upper() not in ('N', 'NO'):
            b = input("ingrese el tipo de animal que desea ingresar (aguila/chita/osopolar) :")
            if b.lower() in ('aguila'):
                self.animales.append(Aguila())
            elif b.lower() in ('chita'):
                self.animales.append(Chita())
            elif b.lower() in ('osopolar'):
                self.animales.append(OsoPolar())
            else:
                print("Incorrecto")
            a = input('¿Quieres continuar? (S/N): ')
        return self

zoo1 = Zoo("Metropolitano")
zoo1.addmasivo()
zoo1.print_all_info()
input("Presione ENTER para salir")
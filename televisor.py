class Televisor:
    def __init__(self, marca, tamaño, lista_canales):
        self.Marca = marca
        self.Tamaño = tamaño
        self.Canal_actual = "Ninguno" 
        self.Volumen = 10
        self.Encendido = False
        self.Lista_canales = ["La 1","Antena 3","Telecinco","Canal Sur","La 2"]
    
    def encender_apagar(self):
        if self.Encendido == True:
            self.Encendido = False
            print("El televisor se ha apagado.")
        else:
            self.Encendido = True
            print("El televisor se ha encendido.")
    
    def subir_volumen(self):
        if self.Encendido:
            if self.Volumen < 100:
                self.Volumen += 5
                print(f"Volumen aumentado a {self.Volumen}.")
            else:
                print("El volumen ya está al mínimo.")
    
    def bajar_volumen(self):
        if self.Encendido:
            if self.Volumen > 0:
                self.Volumen -= 5
                print(f"Volumen disminuido a {self.Volumen}.")
            else:
                print("El volumen ya está al mínimo.")
    
    def cambiar_canal(self,canal):
        if self.Encendido:
            if canal in self.Lista_canales:
                self.Canal_actual = canal
                print(f"Canal cambiado a: {self.Canal_actual}.")
            else:
                print(f"El canal {canal} seleccionado no está disponible.")
        else:
            print("El televisor está apagado enciendelo para cambiar de canal.")
    
    def mostrar_info(self):
        if self.Encendido == True:
            print(f"Marca: {self.Marca}")
            print(f"Tamaño: {self.Tamaño} pulgadas")
            print(f"Canal actual: {self.Canal_actual}")
            print(f"Volumen: {self.Volumen}")
            print(f"Estado: {self.Encendido}")
        else:
            print("El televisor está apagado. Enciéndelo para ver la información.")
    
    def agregar_canal(self,canal):
        if canal not in self.Lista_canales:
            self.Lista_canales.append(canal)
            print(f"El canal '{canal}' se ha agregado a la lista.")
        else:
            print(f"El canal '{canal}' ya está en la lista.")
    
    def eliminar_canal(self,canal):
        if canal in self.Lista_canales:
            self.Lista_canales.remove(canal)
            print(f"El canal '{canal}' se ha borrado de la lista.")
        else:
            print(f"El canal '{canal}' no está en la lista.")

Televisor1 = Televisor("Samsung",22,"Antena 3")
Televisor1.encender_apagar()
Televisor1.subir_volumen()
Televisor1.bajar_volumen()
Televisor1.cambiar_canal("Antena 3") 

print("\n")

Televisor1.mostrar_info()
Televisor1.agregar_canal("Neox")
Televisor1.eliminar_canal("La 1")

print("\n")

Televisor1.mostrar_info()

print("\n")

Televisor1.cambiar_canal("La 1")

print("\n")

Televisor1.mostrar_info()
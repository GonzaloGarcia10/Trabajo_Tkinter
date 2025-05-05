import tkinter as tk
from tkinter import messagebox, Toplevel

class Televisor:
    def __init__(self, marca, tamaño, lista_canales):
        self.Marca = marca
        self.Tamaño = tamaño
        self.Canal_actual = "Ninguno" 
        self.Volumen = 0
        self.Encendido = False
        self.Lista_canales = ["La1", "La2", "Antena3", "Cuatro", "Telecinco", "La-Sexta", "Canal-Sur", "Boing", "Neox"]
    
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
                print("El volumen ya está al máximo.")
    
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
            print("El televisor está apagado, enciéndelo para cambiar de canal.")
    
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

televisor = Televisor("Samsung", 22, ["La1", "La2", "Antena3", "Cuatro", "Telecinco", "La-Sexta", "Canal-Sur", "Boing", "Neox"])

ventana = tk.Tk()
ventana.geometry("800x580")
ventana.title("Televisión")
ventana.resizable(False, False)
ventana.config(bg="#2f2f2f")

titulo = tk.Label(ventana, text="Samsung TV", font=("Arial", 20, "bold"), fg="white", bg="#2f2f2f")
titulo.place(x=320, y=10)

canal_label = tk.Label(ventana, text="Canal Actual: Ninguno", font=("Arial", 15, "bold"), fg="white", bg="#2f2f2f")
canal_label.place(x=530, y=480)

volumen_label = tk.Label(ventana, text=f"Volumen: {televisor.Volumen}", font=("Arial", 15, "bold"), fg="white", bg="#2f2f2f")
volumen_label.place(x=70, y=480)

tv_frame = tk.Frame(ventana, bg="black")
tv_frame.place(x=50, y=70)

imagen_negra = tk.PhotoImage(file="black.png")
labelfoto = tk.Label(tv_frame, image=imagen_negra)
labelfoto.pack(expand=True)

def mostrar_imagen(canal):
    try:
        imagen = tk.PhotoImage(file=f"{canal}.png")
    except:
        imagen = imagen_negra
    labelfoto.config(image=imagen)
    labelfoto.image = imagen

def subir_volumen():
    televisor.subir_volumen()
    volumen_label.config(text=f"Volumen: {televisor.Volumen}")

def bajar_volumen():
    televisor.bajar_volumen()
    volumen_label.config(text=f"Volumen: {televisor.Volumen}")

def encendido_apagado():
    televisor.encender_apagar()

    if televisor.Encendido:
        televisor.Canal_actual = "La1"
        imagen_por_defecto = tk.PhotoImage(file="La1.png")
        labelfoto.config(image=imagen_por_defecto)
        labelfoto.image = imagen_por_defecto
        lista_canales.place(x=600, y=530)
        canal_label.config(text=f"Canal Actual: {televisor.Canal_actual}") 
    else:
        labelfoto.config(image=imagen_negra)
        labelfoto.image = imagen_negra
        lista_canales.place_forget()
        canal_label.config(text="Canal Actual: Apagado")

def abrir_lista_canales():
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.geometry("500x470")
    ventana_secundaria.title("Canales")
    ventana_secundaria.resizable(False, False)
    ventana_secundaria.config(bg="#2f2f2f")

    def mostrar_seleccion():
        try:
            seleccion = lista.get(lista.curselection())  
            print("Canal seleccionado:", seleccion)
            televisor.cambiar_canal(seleccion)
            canal_label.config(text=f"Canal Actual: {televisor.Canal_actual}")
            mostrar_imagen(seleccion)
        except:
            print("Error: No has seleccionado ningún canal.")
    
    lista = tk.Listbox(ventana_secundaria,bg="#2f2f2f",font=("Arial", 15, "bold"),fg="white")
    lista.pack()

    for canal in televisor.Lista_canales:
        lista.insert(tk.END, canal)

    entrada = tk.Entry(ventana_secundaria,bg="#2f2f2f",font=("Arial", 15, "bold"),fg="white")
    entrada.pack()

    def agregar():
        canal = entrada.get()
        if canal in televisor.Lista_canales:
            tk.messagebox.showerror("Error", f"El canal '{canal}' ya está en la lista.") 
        else:
            televisor.agregar_canal(canal) 
            lista.insert(tk.END, canal) 
            entrada.delete(0, tk.END) 

    def eliminar():
        try:
            canal = lista.get(lista.curselection()) 
            televisor.eliminar_canal(canal)  
            lista.delete(lista.curselection())  
        except:
            print("Error: No has seleccionado ningún canal.")
            tk.messagebox.showerror("Error:","No has seleccionado ningún canal.")

    tk.Button(ventana_secundaria, text="Agregar", command=agregar,font=("Arial", 15, "bold")).place(x=200,y=355)
    tk.Button(ventana_secundaria, text="Eliminar", command=eliminar,font=("Arial", 15, "bold")).place(x=200,y=410)
    tk.Button(ventana_secundaria, text="Seleccionar", command=mostrar_seleccion,font=("Arial", 15, "bold")).place(x=185,y=300)
    boton_subir_volumen = tk.Button(ventana, text="+🔊", font=("Arial", 20), command=subir_volumen)
    boton_subir_volumen.place(x=155, y=515)
    boton_bajar_volumen = tk.Button(ventana, text="-🔉", font=("Arial", 20), command=bajar_volumen)
    boton_bajar_volumen.place(x=240, y=515)

lista_canales = tk.Button(ventana, text="Lista de Canales", font=("Arial", 15, "bold"), command=abrir_lista_canales)
tk.Button(ventana, text="Cerrar", font=("Arial", 15, "bold"), command=ventana.quit).place(x=20, y=530)
imagen_encender = tk.PhotoImage(file="encender-apagar.png")  
apagar_encender = tk.Button(ventana, image=imagen_encender, bd=0, highlightthickness=0, relief="flat",overrelief="flat", activebackground="#2f2f2f", background="#2f2f2f", command=encendido_apagado).place(x=360, y=495)  

ventana.mainloop()


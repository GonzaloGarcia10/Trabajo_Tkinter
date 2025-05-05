import tkinter
import tkinter.messagebox

ventana = tkinter.Tk() # Crea la ventana principal
ventana.geometry("800x580") #Ancho = 500 px, Alto = 300 px
ventana.title("Mi aplicación Tkinter") #Cambiar el título de la ventana.

tkinter.Label(ventana,text="Hola").pack() #Muestra texto o imágenes
# tkinter.Button(ventana,text="Click",command=funcionQueHaceAlgo).pack() Boton interactivo
tkinter.Entry(ventana).pack() # Campo de texto de una línea
tkinter.Text(ventana).pack() # Área de texto multilínea
tkinter.Frame(ventana).pack() # Contenedor para agrupar widgets

def saludar():
    print("¡Hola, mundo!")

tkinter.Button(ventana, text="Saludar", command=saludar).pack()

def tecla_presionada(event):
    print(f"Tecla presionada: {event.char}")

ventana.bind("<Key>", tecla_presionada)

def mostrar_coordenadas(event):
    print(f"Coordenadas: ({event.x}, {event.y})")

ventana.bind("<Motion>", mostrar_coordenadas) # Detecta movimiento del ratón

tkinter.messagebox.showinfo("Mensaje de info")
tkinter.messagebox.showwarning("Mensaje de adver")
tkinter.messagebox.showerror("Mensaje de err")

ventana.mainloop()








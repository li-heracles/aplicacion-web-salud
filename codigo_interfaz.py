# Aqui estara el codigo para la interfaz
from tkinter import *
from tkinter import ttk

#Para importar custom tkinter
import customtkinter

root = tk()
# Creación de un cuadro
frame = tkk.frame(parent)

# Especificar altura y anchura del cuadro
frame['width'] = 600
frame['height'] = 400

# Especificar distancia en pantalla del cuadro (se mide en pixeles)
frame['width'] = '500p'

# Relleno del marco entre su borde y los widgets
frame['padding'] = (5,10) 

# Muestra un borde alrederdor del marco (anchura y aparaciencia visual del borde)
frame['borderwidth'] = 2 
frame['relief'] = 'sunken'

# Etiqueta (para mostrar texto e imagenes sin interactuar)
label = ttk.label(parent, text='nombre usuario:')

# Mostrar texto (solo permite adjuntar widgets a una instancia de clase string)
resultsContents = Stringvar()
labels['textvariable'] = results contents
resultsContents.set('Valor inicial para mostrar')

# uso de get y set para leer y escribir el valor actual de la variable
current = resultsContents.get()
resultsContents.set('nuevo valor a mostrar')

#agregar imagen 
image = PhotoImage(file='Myimage.png')
label['image'] = image

#
label['font'] = "TKDefaultFont"

# entrada (ingresar texto)
nombre_usuario = stringvar()
nombre = ttk.entry(parent, textvariable=nombre_usuario)

# Agregar numero de caracteres a la entrada 
nombre['width'] = 30

# agregar contraseña
contrase = ttk.entry(parent, textvariable=password, show="*")

#colores a usar 
#fire brick
#agua
#turquesa

#barra de movimiento
barmov = ttk.scrollbar( parent, orient=vertical, comand=listbox.yview)
listbox.configure(yscrollcommand= set)


examenvar = Stringvar()
examen =ttk.Combox(parent, textvariable=examenvar)
examen['values'] = ['Traumatología','Obesidad y Nutrición','Ginecologia y Obtetricia')
examen.state(["readonly")]

import random
import string
import tkinter as tk
from PIL import ImageTk, Image
from languages.lang import get_translation
from tkinter import PhotoImage
import webbrowser

#Generador de contraseñas
def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation 
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

#Creando función generar contraseñas
def generar():
    longitud = int(longitud_var.get())
    contrasena_generada = generar_contrasena(longitud)
    contrasenas_text.config(state=tk.NORMAL)  #Habilitar edición
    contrasenas_text.delete("1.0", tk.END)
    contrasenas_text.insert(tk.END, contrasena_generada)
    contrasenas_text.config(state=tk.DISABLED)  #Deshabilitar edición después de mostrar la contraseña


#Tamaño de ventana
root = tk.Tk()
root.title("Password Generator v1.0")
root.geometry("315x250")
root.aspect(4, 3, 4, 3)  #Establecer relación de aspecto inicial 4:3
root.configure(bg='#83838B')


#Switch de idioma predeterminado (el principal)
idioma_var = tk.StringVar()
idioma_var.set("es")  #Valor predeterminado

def cambiar_idioma(idioma):
    translation = get_translation(idioma)
    titulo_label.config(text=translation["title"])
    longitud_label.config(text=translation["password_length"])
    opcion_12.config(text=translation["length_12"])
    opcion_16.config(text=translation["length_16"])
    opcion_20.config(text=translation["length_20"])
    generar_button.config(text=translation["generate"])


def cambiar_idioma_es():
    cambiar_idioma("es")

def cambiar_idioma_eng():
    cambiar_idioma("eng")

def cambiar_idioma_cn():
    cambiar_idioma("cn")


#Creando función linkear redes
def abrir_github():
    webbrowser.open("https://github.com/choripanycristi")

def abrir_twitter():
    webbrowser.open("https://twitter.com/choripanycristi")

def abrir_speedrun():
    webbrowser.open("https://speedrun.com/choripanycristi")

#Título
titulo_label = tk.Label(root, text="Password Generator v1.0", font=("Helvetica", 13, "bold"), bg="#83838B")
titulo_label.pack(pady=10)


#Etiquetas y opciones de longitud
longitud_label = tk.Label(root, text="Password length:", bg="#83838B")
longitud_label.pack()

longitud_var = tk.StringVar()
longitud_var.set("12")  #Valor predeterminado

opcion_12 = tk.Radiobutton(root, text="12 characters", variable=longitud_var, value="12", bg="#83838B") 
opcion_12.pack()

opcion_16 = tk.Radiobutton(root, text="16 characters", variable=longitud_var, value="16", bg="#83838B")
opcion_16.pack()

opcion_20 = tk.Radiobutton(root, text="20 characters", variable=longitud_var, value="20", bg="#83838B")
opcion_20.pack()

#Botón para generar contraseñas
generar_button = tk.Button(root, text="Generate", command=generar, bg="#E0E0EE")
generar_button.pack(pady=10)

#Área de texto para mostrar las contraseñas generadas
contrasenas_text = tk.Text(root, height=1, width=30, font=("Courier", 12), state=tk.DISABLED)
contrasenas_text.pack()

#Botones de idioma
es_image = ImageTk.PhotoImage(Image.open("languages/img/es.png"))  # Reemplaza "es.png" con la ruta correcta a la imagen de la bandera para el idioma español
es_button = tk.Button(root, image=es_image, command=cambiar_idioma_es, bg="#C1C1CD")
es_button.pack(side="left", padx=3, pady=7)

eng_image = ImageTk.PhotoImage(Image.open("languages/img/en.png"))  # Reemplaza "en.png" con la ruta correcta a la imagen de la bandera para el idioma inglés
eng_button = tk.Button(root, image=eng_image, command=cambiar_idioma_eng, bg="#C1C1CD")
eng_button.pack(side="left", padx=3, pady=7)

cn_image = ImageTk.PhotoImage(Image.open("languages/img/cn.png"))  # Reemplaza "cn.png" con la ruta correcta a la imagen de la bandera para el idioma chino
cn_button = tk.Button(root, image=cn_image, command=cambiar_idioma_cn, bg="#C1C1CD")
cn_button.pack(side="left", padx=3, pady=7)


#Redes sociales
github_image = ImageTk.PhotoImage(Image.open("socials/git.png"))  
twitter_image = ImageTk.PhotoImage(Image.open("socials/tw.png"))  
speedrun_image = ImageTk.PhotoImage(Image.open("socials/src.png"))

src_button = tk.Button(root, image=speedrun_image, command=abrir_speedrun, bg="#C1C1CD")
src_button.pack(side="right", pady=5, padx=2)

twitter_button = tk.Button(root, image=twitter_image, command=abrir_twitter, bg="#C1C1CD")
twitter_button.pack(side="right", pady=1, padx=2)

github_button = tk.Button(root, image=github_image, command=abrir_github, bg="#C1C1CD")
github_button.pack(side="right", pady=5, padx=2)


root.mainloop()
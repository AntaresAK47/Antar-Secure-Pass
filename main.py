import random
import string
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generar_contraseña(longitud=12, incluir_mayusculas=False, incluir_numeros=False, incluir_simbolos=False):
    """Genera una contraseña aleatoria de la longitud especificada."""
    caracteres = string.ascii_lowercase  # Siempre incluir letras minúsculas

    if incluir_mayusculas:
        caracteres += string.ascii_uppercase  # Incluir mayúsculas
    if incluir_numeros:
        caracteres += string.digits  # Incluir números
    if incluir_simbolos:
        caracteres += string.punctuation  # Incluir símbolos

    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

def generar_clave():
    """Genera una clave de encriptación."""
    return Fernet.generate_key()

def encriptar_contraseña(contraseña, clave):
    """Encripta la contraseña usando una clave."""
    fernet = Fernet(clave)
    contraseña_encriptada = fernet.encrypt(contraseña.encode())
    return contraseña_encriptada

def desencriptar_contraseña(contraseña_encriptada, clave):
    """Desencripta la contraseña usando una clave."""
    fernet = Fernet(clave)
    contraseña_desencriptada = fernet.decrypt(contraseña_encriptada).decode()
    return contraseña_desencriptada

# Funciones para la UI
def generar_y_mostrar_contraseña():
    """Genera y muestra la contraseña en la interfaz."""
    try:
        longitud = int(entry_longitud.get())  # Obtiene la longitud de la entrada
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese una longitud válida.")
        return

    incluir_mayusculas = var_mayusculas.get()  # Obtener estado del checkbox de mayúsculas
    incluir_numeros = var_numeros.get()  # Obtener estado del checkbox de números
    incluir_simbolos = var_simbolos.get()  # Obtener estado del checkbox de símbolos

    contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)
    clave = generar_clave()

    contraseña_encriptada = encriptar_contraseña(contraseña, clave)
    contraseña_desencriptada = desencriptar_contraseña(contraseña_encriptada, clave)

    # Mostrar los resultados en las etiquetas
    label_contraseña.config(text=f"Contraseña generada: {contraseña}")
    label_encriptada.config(text=f"Contraseña encriptada: {contraseña_encriptada.decode()}")
    label_desencriptada.config(text=f"Contraseña desencriptada: {contraseña_desencriptada}")
    label_clave.config(text=f"Clave de encriptación: {clave.decode()}")


# Función para copiar al portapapeles
def copiar_al_portapapeles(contraseña):
    pyperclip.copy(contraseña)
    messagebox.showinfo("Información", "Contraseña copiada al portapapeles.")


# Crear la ventana de la interfaz gráfica
root = tk.Tk()
root.title("Generador de Contraseñas Seguras")
root.configure(bg="#2E2E2E")
root.geometry("500x600")
label_longitud = tk.Label(root, text="Longitud de la contraseña:", bg="#2E2E2E", fg="white")
label_longitud.pack(pady=5)

entry_longitud = tk.Entry(root)
entry_longitud.pack(pady=5)
var_mayusculas = tk.BooleanVar()
checkbox_mayusculas = tk.Checkbutton(root, text="Incluir mayúsculas", variable=var_mayusculas, bg="#2E2E2E", fg="white")
checkbox_mayusculas.pack(pady=5)

var_numeros = tk.BooleanVar()
checkbox_numeros = tk.Checkbutton(root, text="Incluir números", variable=var_numeros, bg="#2E2E2E", fg="white")
checkbox_numeros.pack(pady=5)

var_simbolos = tk.BooleanVar()
checkbox_simbolos = tk.Checkbutton(root, text="Incluir símbolos", variable=var_simbolos, bg="#2E2E2E", fg="white")
checkbox_simbolos.pack(pady=5)
boton_generar = tk.Button(root, text="Generar Contraseña", command=generar_y_mostrar_contraseña, bg="#FF5733",
                          fg="white")
boton_generar.pack(pady=10)
label_contraseña = tk.Label(root, text="Contraseña generada: ", bg="#2E2E2E", fg="white")
label_contraseña.pack(pady=5)

label_encriptada = tk.Label(root, text="Contraseña encriptada: ", bg="#2E2E2E", fg="white")
label_encriptada.pack(pady=5)

label_desencriptada = tk.Label(root, text="Contraseña desencriptada: ", bg="#2E2E2E", fg="white")
label_desencriptada.pack(pady=5)

label_clave = tk.Label(root, text="Clave de encriptación: ", bg="#2E2E2E", fg="white")
label_clave.pack(pady=5)

boton_copiar = tk.Button(root, text="Copiar Contraseña",
                         command=lambda: copiar_al_portapapeles(label_contraseña.cget("text")[20:]), bg="#FF5733",
                         fg="white")
boton_copiar.pack(pady=10)
root.mainloop()

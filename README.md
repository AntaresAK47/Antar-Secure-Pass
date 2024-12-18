# Antar-Secure-Pass
Secure, open source password creation and encryption environment.
# Generador de Contraseñas Seguras

Este es un proyecto en Python que permite generar contraseñas aleatorias seguras y encriptarlas utilizando una clave de encriptación. El proyecto incluye una interfaz gráfica de usuario (GUI) basada en `tkinter` para facilitar la interacción con el programa. Además, se integra con `pyperclip` para copiar las contraseñas generadas al portapapeles.

## Características

- **Generación de contraseñas seguras**: Genera contraseñas aleatorias con caracteres alfanuméricos y símbolos.
- **Encriptación de contraseñas**: Las contraseñas generadas pueden ser encriptadas con una clave única utilizando el algoritmo `Fernet` de la biblioteca `cryptography`.
- **Desencriptación de contraseñas**: Las contraseñas encriptadas pueden ser desencriptadas de vuelta a su forma original.
- **Interfaz gráfica de usuario (GUI)**: Implementada con `tkinter` para facilitar la interacción del usuario.
- **Copiar al portapapeles**: Se integra con `pyperclip` para copiar la contraseña generada al portapapeles de manera sencilla.
- **Personalización**: Permite al usuario configurar la longitud de la contraseña y elegir si incluir mayúsculas, números y símbolos en las contraseñas generadas.

## Requisitos

- **Python 3.x** (Recomendado: versión 3.7 o superior)
- Bibliotecas de Python:
  - `cryptography`
  - `tkinter` (viene preinstalada con Python)
  - `pyperclip`

Puedes instalar las dependencias utilizando `pip`:

```bash
pip install -r requirements.txt
Enjoy!

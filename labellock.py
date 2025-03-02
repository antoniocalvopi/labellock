"""
Este script implementa un sistema de cifrado y descifrado sencillo usando XOR con una clave privada.

El funcionamiento básico es el siguiente:
1. El texto se convierte en valores ASCII.
2. Se aplica una operación XOR con la clave (que puede ser numérica o alfabética).
3. El texto cifrado o descifrado se devuelve en forma de una lista de números separados por guiones.

Funciones principales:
- `xor_cipher`: Función que aplica la operación XOR entre el texto y la clave.
- `encrypt`: Función que cifra el texto usando la clave.
- `decrypt`: Función que descifra el texto cifrado usando la clave.
"""
import tkinter as tk

def xor_cipher(text, key):
    """Aplica XOR entre el texto y la clave (se repite en bucle si la clave es más corta)."""
    return [ord(char) ^ ord(key[i % len(key)]) for i, char in enumerate(text)]

def encrypt(text, key):
    """Cifra el texto convirtiéndolo en una lista de números."""
    encrypted = xor_cipher(text, key)
    return "-".join(map(str, encrypted))  # Convierte los números en una cadena separada por guiones

def decrypt(encrypted_text, key):
    """Descifra la lista de números volviendo al texto original."""
    encrypted_numbers = list(map(int, encrypted_text.split("-")))  # Convierte la cadena en números
    decrypted_chars = [chr(num ^ ord(key[i % len(key)])) for i, num in enumerate(encrypted_numbers)]
    return "".join(decrypted_chars)

def run_gui():
    """Función para ejecutar la interfaz gráfica."""
    def on_submit():
        """Procesa la entrada y realiza el cifrado o descifrado."""
        text = text_entry.get()
        key = key_entry.get()
        mode = mode_var.get()

        if mode == "c":
            result = encrypt(text, key)
            result_label.config(text=f"Texto cifrado: {result}")
        elif mode == "d":
            result = decrypt(text, key)
            result_label.config(text=f"Texto descifrado: {result}")
        else:
            messagebox.showerror("Error", "Opción no válida. Usa 'c' para cifrar o 'd' para descifrar.")

    root = tk.Tk()
    root.title("Cifrado XOR con Clave Privada")

    # Entrada de texto
    tk.Label(root, text="Introduce el texto:").pack(pady=5)
    text_entry = tk.Entry(root, width=50)
    text_entry.pack(pady=5)

    # Entrada de clave
    tk.Label(root, text="Introduce la clave privada:").pack(pady=5)
    key_entry = tk.Entry(root, width=50)
    key_entry.pack(pady=5)

    # Modo (cifrar o descifrar)
    mode_var = tk.StringVar(value="c")  # 'c' por defecto (cifrar)
    tk.Label(root, text="Selecciona el modo:").pack(pady=5)
    tk.Radiobutton(root, text="Cifrar", variable=mode_var, value="c").pack(pady=5)
    tk.Radiobutton(root, text="Descifrar", variable=mode_var, value="d").pack(pady=5)

    # Botón para ejecutar la operación
    tk.Button(root, text="Ejecutar", command=on_submit).pack(pady=20)

    # Etiqueta para mostrar resultados
    result_label = tk.Label(root, text="", fg="blue")
    result_label.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    run_gui()


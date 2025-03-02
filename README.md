# LabelLock - XOR Cipher with Private Key

## Descripción

Este proyecto implementa un cifrado y descifrado sencillo utilizando la operación XOR con una clave privada. El sistema convierte texto en números utilizando el valor ASCII de cada carácter y una clave proporcionada por el usuario. Se puede ejecutar tanto en modo consola como con una interfaz gráfica simple utilizando **Tkinter**.

## Características

- **Cifrado y descifrado con clave privada** usando la operación XOR.
- **Interfaz gráfica** con un botón para cambiar entre modo consola y modo gráfico.
- Texto cifrado/desifrado representado en valores numéricos para mayor seguridad y discreción, sobre todo discreción más que seguridad :).

## Requisitos

- Python 3.x
- Tkinter (generalmente preinstalado en Python 3)

## Instalación

Para instalar y ejecutar el proyecto, sigue estos pasos:

1. Clona el repositorio:

   ```bash
   git clone [https://github.com/tu-usuario/xor-cipher.git](https://github.com/antoniocalvopi/labellock)
   cd labellock
   ```

2. (Opcional-RECOMENDABLE) Crea un entorno virtual y actívalo:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   ```

3. Instala las dependencias (si fuera necesario):

   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta el programa:

   ```bash
   python labellock.py
   ```

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar el código, crear nuevos métodos de cifrado, o arreglar errores, por favor crea un *pull request*.

1. Haz un fork de este repositorio.
2. Crea una nueva rama (`git checkout -b feature-nueva-caracteristica`).
3. Haz tus cambios y comités (`git commit -am 'Agrega nueva característica'`).
4. Empuja a tu rama (`git push origin feature-nueva-caracteristica`).
5. Crea un *pull request*.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

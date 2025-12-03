# Ejemplo de Encapsulación
# La encapsulación agrupa datos y métodos, restringiendo el acceso directo a los atributos.

class Persona:
    def __init__(self, nombre):
        # El doble guion bajo (__nombre) hace que el atributo sea PRIVADO.
        # Python "oculta" esta variable para que no sea accesible fácilmente desde fuera.
        self.__nombre = nombre

    def get_nombre(self):
        """Getter: Permite leer el atributo privado."""
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        """Setter: Permite modificar el atributo privado bajo ciertas reglas."""
        # Validación: Solo cambiamos el nombre si no está vacío.
        # Esto protege la integridad de los datos del objeto.
        if nuevo_nombre and len(nuevo_nombre) > 0:
            self.__nombre = nuevo_nombre
        else:
            print("Error: El nombre no puede estar vacío.")

# --- Ejecución del código ---
print("--- Inicio del ejemplo de Encapsulación ---")
p = Persona("Juan")

# Intentamos acceder correctamente a través del Getter
print(f"Nombre inicial: {p.get_nombre()}")

# Modificamos el nombre a través del Setter (forma correcta)
p.set_nombre("Ana")
print(f"Nombre modificado: {p.get_nombre()}")

# Intentamos poner un nombre inválido para probar la protección del Setter
p.set_nombre("") # Esto imprimirá un error y no cambiará el nombre

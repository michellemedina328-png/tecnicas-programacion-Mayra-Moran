# Ejemplo de Herencia
# La herencia permite crear nuevas clases basadas en clases existentes (reutilización de código).

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        """Método base que será sobrescrito por las clases hijas."""
        print(f"{self.nombre} hace un sonido genérico.")

class Perro(Animal):
    # La clase Perro hereda todo de Animal
    def hacer_sonido(self):
        # Sobrescritura de método (Override): Cambiamos el comportamiento original
        print(f"{self.nombre} dice: ¡Guau!")

# --- Ejecución del código ---
print("--- Inicio del ejemplo de Herencia ---")

# Instanciamos la clase padre
animal_generico = Animal("Criatura")
animal_generico.hacer_sonido()

# Instanciamos la clase hija
mi_perro = Perro("Firulais")
# El objeto 'mi_perro' tiene el atributo nombre y el método hacer_sonido
mi_perro.hacer_sonido()

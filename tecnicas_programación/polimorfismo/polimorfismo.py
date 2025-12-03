# Ejemplo de Polimorfismo
# El polimorfismo permite que objetos de diferentes clases respondan al mismo mensaje (método) de formas distintas.

class Animal:
    def hacer_sonido(self):
        pass # Método abstracto simulado

class Perro(Animal):
    def hacer_sonido(self):
        print("El perro hace: ¡Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("El gato hace: ¡Miau!")

class Vaca(Animal):
    def hacer_sonido(self):
        print("La vaca hace: ¡Muu!")

# Función externa que demuestra el polimorfismo
def reproducir_sonido(animal):
    # No importa si es Perro, Gato o Vaca, todos son 'Animal' y saben 'hacer_sonido'
    animal.hacer_sonido()

# --- Ejecución del código ---
print("--- Inicio del ejemplo de Polimorfismo ---")

# Creamos una lista con diferentes tipos de objetos
mis_animales = [Perro(), Gato(), Vaca()]

# Iteramos sobre la lista tratando a todos por igual
for a in mis_animales:
    reproducir_sonido(a)

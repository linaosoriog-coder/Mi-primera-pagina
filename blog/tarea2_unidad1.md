# Tarea 2 - Ejercicios Unidad 1

Aquí iré agregando mis soluciones a los ejercicios de la Unidad 1.

## Reto 1: Simular el comportamiento de la tortuga con texto
**Enunciado:**  
Simular el movimiento de una tortuga usando solo `print()` e `input()`.

```python
pasos = int(input("¿Cuántos pasos debe avanzar la tortuga? "))

for i in range(pasos):
    print("🐢 →")
Explicación:
Este programa pide al usuario cuántos pasos debe avanzar la tortuga y luego imprime ese número de movimientos hacia la derecha usando un ciclo for.

Reto 2: Tortuga bajando

Enunciado:
Crear el rastro de una tortuga moviéndose hacia abajo usando solo print() e input().
pasos = int(input("¿Cuántos pasos debe bajar la tortuga? "))

for i in range(pasos):
    print("🐢")
Explicación:
El programa pide cuántos pasos debe bajar la tortuga y los dibuja en forma vertical usando varias líneas.

Reto 3: Girar y dibujar usando solo print() e input()

Enunciado:
La tortuga avanza, gira a la derecha y vuelve a avanzar, formando una L.
horizontal = int(input("Pasos hacia la derecha: "))
vertical = int(input("Pasos hacia abajo después de girar: "))

for i in range(horizontal):
    print("→", end="")

print()  # salto de línea

for i in range(vertical):
    print("↓")
Explicación:
Primero se dibuja el movimiento horizontal con flechas a la derecha. Luego, después del giro, se dibujan los pasos hacia abajo.

Reto 4: Encapsular los movimientos usando funciones

Enunciado:
Crear funciones adelante(n) y abajo(n) para dibujar la tortuga.
def adelante(n):
    for i in range(n):
        print("→", end="")
    print()

def abajo(n):
    for i in range(n):
        print("↓")

adelante(5)
abajo(3)
Explicación:
Se crean dos funciones: una para mover la tortuga hacia la derecha y otra hacia abajo. Luego se usan para formar una figura en forma de L.

Reto 5: La tortuga baja las escalas

Enunciado:
La tortuga debe bajar varios escalones conservando la posición horizontal.
def adelante(n):
    for i in range(n):
        print("→", end="")
    print()

def abajo(n):
    for i in range(n):
        print("↓")

# Escalón 1
adelante(5)
abajo(2)

# Escalón 2
adelante(5)
abajo(2)

# Escalón 3
adelante(5)
abajo(2)
Explicación:
Se reutilizan las funciones adelante() y abajo() para construir una escalera, donde cada escalón tiene un tramo horizontal y uno vertical.

Referencias de IA

ChatGPT: Apoyo en la solución, estructura del código y explicaciones de los ejercicios de la Unidad 1.

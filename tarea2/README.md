# 🐢 Tarea 2 – Ejercicios Unidad 1

## Aprendiendo a programar como una tortuga

---

## 📘 Introducción

En esta actividad se desarrollan una serie de retos orientados a fortalecer los conceptos básicos de programación en Python, haciendo uso exclusivo de las funciones `print()` e `input()`.
A través de la simulación del movimiento de una tortuga usando texto, se refuerzan habilidades como el manejo de variables, entrada de datos, control del flujo del programa y organización del código.

Los ejercicios se presentan de forma progresiva, comenzando con movimientos simples y finalizando con una simulación más compleja mediante funciones y acumulación de espacios, lo cual permite una mejor comprensión de la lógica de programación.

---

## 🐢 Reto 1: Simular el comportamiento de la tortuga

**Enunciado:**
Simular el movimiento de una tortuga usando solo `print()` e `input()`.

Este es el código para avanzar y pedir el número de pasos (`n`):

```python
# Representa la tortuga mirando hacia la derecha
tortuga = ">"

# Solicita al usuario el número de pasos hacia adelante
pasos_adelante = int(input("Ingrese el número de pasos hacia adelante: "))

# Dibuja el recorrido horizontal de la tortuga
print("- " * pasos_adelante + tortuga)
```

### ✅ Solución en Python

![Solución Reto 1](https://github.com/user-attachments/assets/789976c5-0750-4ed5-9eee-c0da0712675c)

---

## 🐢 Reto 2: Tortuga bajando

**Enunciado:**
Crea el rastro de una tortuga moviéndose hacia abajo usando únicamente `print()` e `input()`.

Este es el código para bajar y pedir el número de pasos (`n`):

```python
# Representa la tortuga mirando hacia abajo
tortuga = "v"

# Solicita al usuario el número de pasos hacia abajo
pasos_abajo = int(input("Ingrese el número de pasos hacia abajo: "))
print("|\n" * pasos_abajo + tortuga)
```

### ✅ Solución en Python

![Solución Reto 2](https://github.com/user-attachments/assets/93e67b28-0290-48c4-a945-949e512efedb)

---

## 🐢 Reto 3: Girar y dibujar usando texto

**Enunciado:**
Simula el movimiento: avanzar y luego girar a la derecha para volver a avanzar.

Pide al usuario los pasos hacia adelante y hacia abajo:

```python
# Símbolos que representan la dirección de la tortuga
tortuga = ">"
tortuga_abajo = "v"

pasos_adelante = int(input("Ingrese el número de pasos hacia adelante: "))
print("- " * pasos_adelante + tortuga)

espacios = "  " * pasos_adelante
camino_abajo = espacios + "|\n"

pasos_abajo = int(input("Ingrese el número de pasos hacia abajo: "))
print(camino_abajo * pasos_abajo, end="")
print(espacios + tortuga_abajo)
```

### ✅ Solución en Python

![Solución Reto 3](https://github.com/user-attachments/assets/37e71368-49cf-4d2c-ba02-91f3b2ef327a)

---

## 🐢 Reto 4: Encapsular con funciones

**Enunciado:**
Crear funciones `adelante(n)` y `abajo(n)` que simulen los movimientos.

Reescribe los retos anteriores creando funciones que representen los movimientos de la tortuga solo con texto:

```python
# Símbolos de la tortuga
tortuga = ">"
tortuga_abajo = "v"

# Cantidad de pasos a realizar
adelante = 5   # Movimiento hacia la derecha
abajo = 3      # Movimiento hacia abajo

print("- " * adelante + tortuga)

espacios = "  " * adelante
camino_abajo = espacios + "|\n"
print(camino_abajo * abajo, end="")
print(espacios + tortuga_abajo)
```

### ✅ Solución en Python

![Solución Reto 4](https://github.com/user-attachments/assets/f2ef53f4-64a3-45f7-b6be-ae4cb00749d9)

---

## 🐢 Reto 5: La tortuga baja las escaleras

**Enunciado:**
Ajusta las funciones para que la tortuga baje escalones.

En este reto se utilizan funciones y una variable global para conservar la posición horizontal acumulada. Esto permite simular correctamente una escalera compuesta por varios tramos horizontales y verticales.

```pythonpython
# Variable global para recordar dónde estamos (la sangría)
espacios_acumulados = ""

# --- Definición de las funciones ---

def adelante(pasos):
    global espacios_acumulados
    print(espacios_acumulados + "- " * pasos + ">")
    espacios_acumulados = espacios_acumulados + ("  " * pasos)

def abajo(pasos):
    linea_vertical = espacios_acumulados + "|\n"
    print(linea_vertical * pasos, end="")

# --- EJECUCIÓN DEL DIBUJO ---

# Escalón 1
adelante(5)
abajo(2)

# Escalón 2
adelante(5)
abajo(2)

# Escalón 3
adelante(5)
abajo(2)

# Final
print(espacios_acumulados + "v")
```

### ✅ Solución en Python

![Solución Reto 5](https://github.com/user-attachments/assets/d127f099-fa85-4f9d-9498-ed7f7c57b2ad)

---

## 📝 Conclusión

El desarrollo de estos retos permitió comprender de manera práctica los fundamentos de la programación en Python, como el uso de entradas y salidas, la manipulación de cadenas de texto y la creación de funciones.

La simulación del movimiento de la tortuga facilitó el aprendizaje progresivo de la lógica del programa, pasando de instrucciones simples a estructuras más organizadas y reutilizables. Esta metodología resulta efectiva para afianzar el pensamiento lógico y la resolución de problemas en programación.

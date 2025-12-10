horizontal = int(input("Pasos hacia la derecha: "))
vertical = int(input("Pasos hacia abajo después de girar: "))

for i in range(horizontal):
    print("→", end="")

print()

for i in range(vertical):
    print("↓")
  

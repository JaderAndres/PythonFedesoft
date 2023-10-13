#CONTROL DE FLUJO:

# Practica 1

sec=int(input("Ingrese la cantidad del rango: "))
for num in range(0, 101, sec):
    if num%5==0:
        print(num,  end=", ")
        # num = num + ", "
else:
    print("\nFin del ciclo")

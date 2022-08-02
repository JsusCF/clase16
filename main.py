lista = {"codigo": ["001", "002", "003", "004", "005"], "nombre": ["arroz", "leche", "gaseosa", "aceite", "queso"],
         "precio": [5, 4, 6, 3, 2]}
continuar = True
while continuar:
    codigo = input("Ingrese el codigo del producto ")
    cantidad = int(input("ingrese la cantidad "))
    continuar = input("¿Quieres añadir mas productos? (S/N)") == "s"

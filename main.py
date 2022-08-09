continuar = True
venta = 0
while continuar:
    lista = {"codigo": ["001", "002", "003", "004", "005"], "nombre": ["arroz", "leche", "gaseosa", "aceite", "queso"],
             "precio": [5, 4, 6, 3, 2]}
    print("Lista de Productos")
    print("001 arroz")
    print("002 leche")
    print("003 gaseosa")
    print("004 aceite")
    print("005 queso")
    codigo = input("Ingrese el codigo del producto ")
    cantidad = int(input("ingrese la cantidad "))
    if codigo == "001":
        precio = 5
        producto = "arroz"
    elif codigo == "002":
        precio = 4
        producto = "leche"
    elif codigo == "003":
        precio = 6
        producto = "gaseosa"
    elif codigo == "004":
        precio = 3
        producto = "aceite"
    elif codigo == "005":
        precio = 2
        producto = "queso"
    print("Nombre:", producto)
    print("Cantidad", cantidad)
    preciototal = precio * cantidad
    print("Precio total:", preciototal)
    continuar = input("¿Quieres añadir mas productos? (S/N)") == "s"
    venta += preciototal
    operacion = [str(codigo), " ", producto, " ", str(cantidad), " ", str(precio), " ", str(preciototal)]
    cadena = "".join(operacion)
    f = open("transacciones.txt", "a")
    f.write("\n" + cadena)
    f.close()
f = open("transacciones.txt")
print(f.read())
f.close()
print("El monto total de la venta es:", venta)

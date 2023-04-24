# Construir una función que reciba un valor entero como parámetro y muestra la tabla de multiplicar de dicho valor recibido.  Ejemplo
def generarTabla():
    for i in range(1,11):
        mn = " X "
        ig = " = "
        r = i * n
        print(str(i)+ mn + str(n) + ig + str(r))
    
n = int(input("Escriba el número de la tabla de multiplicar que desea conocer: "))
tabla = "TABLA DEL "
print(tabla + str(n))
generarTabla()
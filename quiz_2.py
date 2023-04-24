# Construir una función que reciba un valor entero como parámetro y que determine si su último dígito es 4.
def revisarUltimoValor():
    if n%10==4:
        print(f"El último dígito es cuatro")
    else:
        print(f"El último dígito no es cuatro")
           
n=int(input("Escriba el número al cual quiere revisar si su último dígito es 4"))
revisarUltimoValor()
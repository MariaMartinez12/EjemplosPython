#Sumar los elementos de un arreglo 
arreglo= []
cant = int(input("DIME CUANTO  #: "))
cont = 0
while(cont <cant):
    num =int(input("Dime un #: "))
    arreglo.append(num)

suma = 0 
for num in arreglo:
    suma +=num
print("La suma es", suma)

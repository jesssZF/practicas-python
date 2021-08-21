#libreria para datos aleatorios
import random
import matplotlib.pyplot as plt

#para instalar la libreria se necesitan los comandos:


#generar numero aleatorio par del 10 al 100
print(random.randrange(10, 100, 2))

#reacomodar una lista al azar
#arreglo
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#imprimir arreglo
print('Lista original',lista)
#reacomoda una lista de datos - el arreglo
random.shuffle(lista)
print('lista mixeada',lista)

#generar campana de gausss
campana = [random.gauss(1, 0.5) for i in range(1000)]
plt.hist(campana, bins=15)
plt.show()
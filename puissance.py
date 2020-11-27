#fonction monExpo
#paramètre les nombres a et n qui sont
#       le nombre et exposant
#renvoit la puissance du nombre
def monExpo(a, n):
    
    return a**n
#fin fonction monExpo

#programme principal
y = 2
x = 6
z = monExpo(x, y) #Appel de la fonction monExpo
print(x, "^",y, " = ",z)
for j in range(1, 11):
    t = monExpo(y, j)
    print(y, "^", j, " = ", t)

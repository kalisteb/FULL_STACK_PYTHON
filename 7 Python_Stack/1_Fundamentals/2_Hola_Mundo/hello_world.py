# 1. TAREA: imprimir "Hola mundo"
print("Hola Mundo")

# 2. imprimir "Hola Noelle!" con el nombre en una variable
name = "Karina"
print("Hola",name,"!") # con una coma
print("Hola "+ name+"!" ) # con un +

# 3. imprimir "Hola 42!" con un numero en una variable
name = 9
print("Hola",name,"!" ) # con una coma
#print("Hola "+ name+"!") # con un + - !Este debería darnos un error!
print("Hola %d!" %9) #NINJA BONUS: descubre cómo resolver el error desde arriba, sin cambiar el signo + a una coma

# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("Me encanta comer {} and {}.".format(fave_food1,fave_food2)) # con .format()
print(f"Me encanta comer {fave_food1} and {fave_food2}.") # con una cadena f

var ="test String"
x=var.partition("String")
print(x)   

y=var.swapcase()
print(y)
 

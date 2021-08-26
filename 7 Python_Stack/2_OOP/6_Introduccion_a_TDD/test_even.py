# importar el marco de prueba de Python
import unittest

# nuestra "unit"
# 1. Ejemplo: esto es lo que estamos ejecutando nuestra prueba en 
def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

#2 escribe una función que invierta los valores en la lista (sin crear una matriz temporal).
def reverseList(arr):
    for i in range(len(arr)//2): 
        temp = arr[i]    
        arr[i] = arr[(len(arr)-i-1)]
        arr[(len(arr)-i-1)] = temp   
    return arr
# 3.  escribe una función que verifique si la palabra dada es palíndrome (una palabra que se lee igual en ambos sentidos).
def isPalindrome(palabra):
    original=0
    aux=0
    for i in reversed(range(0, len(palabra))):
        if palabra[i].lower() == palabra[aux].lower():
            original += 1
        aux += 1
    if len(palabra) == original:
        return True
    else:
        return False 

# 4. monedas : escribe una función que determine cuántas monedas de 25 centavos, de 10 centavos, de 5 centavos y de 1 centavo le dará a un cliente para un cambio en el que minimice la cantidad de monedas que entrega.
def monedas(monto):
    nominaciones=[25, 10, 5, 1]
    cont_monedas=[]
    
    for i in range(len(nominaciones)):
        cont_monedas.append(int(monto/nominaciones[i]))
        monto = int(monto % nominaciones[i]) 
    return cont_monedas    

# 5. BONUS - factorial - Escribe una función recursiva que devuelve el factorial de un número dado. Recuerde que el factorial de un número es el producto de todos los números entre 1 y el número dado (por ejemplo, 4! = 4 * 3 * 2 * 1).
def factorial(num):
    if(num==0):
        return 1
    elif(num<0):
        return "Este número es negativo"
    else:
        return num* factorial(num-1)

# 6. BONUS - fibonacci - Escribe una función recursiva que acepta un número, n, y devuelve el enésimo número de Fibonacci de la secuencia. Los primeros dos números de Fibonacci son 0 y 1. Cada número posterior se calcula sumando los 2 números anteriores de la secuencia. (es decir, 0, 1, 1, 2, 3, 5, 8, 13, 21 ...)

def fibonacci(n):
    if n<0:
        return "Este número es negativo"
    elif n==0 or n==1:
        return n
    else:
        return fibonacci(n-2)+fibonacci(n-1)

# 1. Ejemplo :nuestros "unit tests" 
# inicializado creando una clase que hereda de unittest.TestCase 
class IsEvenTests(unittest.TestCase):
    # cada método en esta clase es una prueba que se ejecutará 
    def testTwo(self):
        self.assertEqual(isEven(2), True)
        # otra forma de escribir arriba es 
        self.assertTrue(isEven(2))
    def testThree(self):
        self.assertEqual(isEven(3), False)
        # otra forma de escribir lo de arriba es
        self.assertFalse(isEven(3))
    #  cualquier tarea que desee ejecutar antes de ejecutar cualquier método anterior, colóquelas en el método setUp 
    def setUp(self):
        # agrega las tareas setUp 
        print("running setUp")
    # cualquier tarea que quieras ejecutar después de ejecutar las pruebas, ponlas en el método
    def tearDown(self):
        # agrega las tareas tearDown 
        print("running tearDown tasks")

# 2.        
class reverseListTests(unittest.TestCase):
    # cada método en esta clase es una prueba que se ejecutará 
    def testOne(self):
        self.assertEqual(reverseList([1,3,5,9,20]), ([20,9,5,3,1]))
    def testTwo(self):
        self.assertEqual(reverseList([-5,-4,-1]), ([-1,-4,-5]))
    def testThree(self):
        self.assertEqual(reverseList(["Coding", "Dojo", "Chile"]), (["Chile", "Dojo", "Coding"]))

# 3.
class isPalindromeTests(unittest.TestCase):
    # cada método en esta clase es una prueba que se ejecutará 
    def testOne(self):
        self.assertEqual(isPalindrome("arenera"), True)
    def testTwo(self):
        self.assertEqual(isPalindrome("ana"), True)
    def testThree(self):
        self.assertFalse(isPalindrome("margarita"), False)
    def testFour(self):
        self.assertEqual(isPalindrome("ojo"), True)
    def testFive(self):
        self.assertFalse(isPalindrome("dia"), False)

# 4.
class monedasTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(monedas(87),([3,1,0,2]))
    def testTwo(self):
        self.assertEqual(monedas(435),([17,1,0,0]))
    def testThree(self):
        self.assertEqual(monedas(1194),([47,1,1,4]))    
    def testFour(self):
        self.assertEqual(monedas(934),([37,0,1,4]))
    def testFive(self):
        self.assertEqual(monedas(693),([27,1,1,3]))
    
# 5. 
class factorialTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(factorial(4), (24))
    def testTwo(self):
        self.assertEqual(factorial(13), (6227020800))
    def testThree(self):
        self.assertEqual(factorial(-3), ("Este número es negativo"))
        
# 6. 
class fibonacciTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(fibonacci(5), (5))
    def testTwo(self):
        self.assertEqual(fibonacci(7), (13))
    def testThree(self):
        self.assertEqual(fibonacci(0), (0))
    def testFour(self):
        self.assertEqual(fibonacci(-5), ("Este número es negativo"))

if __name__ == '__main__':
    unittest.main() # esto ejecuta nuestras pruebas
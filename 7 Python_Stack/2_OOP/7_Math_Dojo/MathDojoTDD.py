import unittest

class MathDojo:
    def __init__(self):
        self.result = 0
        
    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self  

    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self

# crear una instruccion:
md = MathDojo()

# para probar:
#x = md.add(2).add(2,5,1).subtract(3,2).result
#x=md.add(7,5,3).add(8,6,4).add(5,1,7).result
#x=md.add(7,5,3).add(8,6,4).add(5,1,7).subtract(4).subtract(3,2).subtract(4,1,2).result
#print(x)   # debe imprimir 30

class MathDojoTests(unittest. TestCase):
    def setUp(self):
        self.md = MathDojo()
        
    def testAdd(self):
        self.assertEqual(self.md.add(2,4,6,8,10).result,30)
    
    def testSubtract(self):
        self.assertEqual(self.md.subtract(2,4,6,8,10).result,-30)
        
if __name__ == '__main__' :
    unittest.main()
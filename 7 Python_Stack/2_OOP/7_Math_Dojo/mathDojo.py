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
x=md.add(7,5,3).add(8,6,4).add(5,1,7).subtract(4).subtract(3,2).subtract(4,1,2).result

print(x)   # debe imprimir 30

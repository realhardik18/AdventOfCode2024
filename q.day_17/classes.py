import math

class Register:
    def __init__(self, register_a,register_b,register_c):
        self.a=register_a
        self.b=register_b
        self.c=register_c
    def compute_operand(self,x):        
        if x in [0,1,2,3]:
            return x
        elif x==4:
            return self.a
        elif x==5:
            return self.b
        elif x==6:
            return self.c        
    def adv(self,x):
        numerator=self.a
        denominator_power=self.compute_operand(x)
        result=numerator//(math.pow(2,denominator_power))
        self.a=result
    def bxl(self,x):
        self.b=int(self.b)^int(x)
    def bst(self,x):
        self.b=self.compute_operand(x)%8
    def jnz(self, x):
        if self.a != 0:
            return x  
        else:
            return None
    def bxc(self):
        self.b=int(self.b)^int(self.c)
    def out(self,x):
        v=int((self.compute_operand(x)%8))
        print(v)
        return v
    def bdv(self,x):
        numerator=self.a
        denominator_power=self.compute_operand(x)
        result=numerator//(math.pow(2,denominator_power))
        self.b=result        
    def cvd(self,x):    
        numerator=self.a
        denominator_power=self.compute_operand(x)
        result=numerator//(math.pow(2,denominator_power))
        self.c=result  
    def show(self):
        return [int(x) for x in [self.a,self.b,self.c]]




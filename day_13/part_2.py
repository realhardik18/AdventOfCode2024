from helpers import parse_play
from sympy import symbols, Eq, solve
from sympy.core.numbers import Integer as SympyInteger

with open('input.txt','r') as file:
    data=file.read()

plays=data.split('\n\n')
plays=[play.split('\n') for play in plays]
tokens=0

for index,play in enumerate(plays):
    play=parse_play(play)
    x, y = symbols('x,y') 

    n1_x=play[0][0]
    n2_x=play[1][0]
    n1_y=play[0][1]
    n2_y=play[1][1]
    pc_x=play[2][0]+10000000000000
    pc_y=play[2][1]+10000000000000

    eq1 = Eq((n1_x*x+n2_x*y), pc_x) 
    eq2 = Eq((n1_y*x+n2_y*y), pc_y) 

    solution=solve((eq1, eq2), (x, y))
    valid_x=isinstance(solution[x],SympyInteger)
    valid_y=isinstance(solution[y],SympyInteger)
    if valid_x and valid_y:
        tokens+=solution[x]*3+solution[y]*1    
print(tokens)
        
        

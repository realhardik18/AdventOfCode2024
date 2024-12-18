import numpy as np
from classes import Register
with open('input.txt','r') as file:
    d=[l.strip() for l in file.readlines()]

commands=list(map(int,d[-1].split(':')[-1].lstrip().split(',')))

def get_value(a):
    register_a=a
    register_b=0
    register_c=0

    register=Register(register_a,register_b,register_c)    
    pointer=0
    values=[]
    while pointer<len(commands):
        opcode=commands[pointer]
        operand=commands[pointer+1]
        if opcode==0:
            register.adv(operand)
            pointer+=2
        elif opcode==1:
            register.bxl(operand)
            pointer+=2
        elif opcode==2:
            register.bst(x=operand)
            pointer+=2
        elif opcode == 3:
            new_pointer = register.jnz(operand)
            if new_pointer is not None: 
                pointer = new_pointer
            else:  
                pointer += 2
        elif opcode==4:
            register.bxc()
            pointer+=2
        elif opcode==5:
            v=register.out(operand)
            values.append(v)
            pointer+=2        
        elif opcode==6:
            register.bdv(operand)
            pointer+=2
        elif opcode==7:
            register.cvd(operand)
            pointer+=2    
    return values

found=False 
trial_a=1
while not found:
    value=get_value(trial_a)
    if value==commands:
        print('found!!')
        found=True  
    else:
        print(f'defo not {trial_a}')
    trial_a+=1
    



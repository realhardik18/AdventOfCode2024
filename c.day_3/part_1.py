import re
with open('input.txt','r') as file:
    data=file.read()

def multiply(text):
    operations=re.findall(r'mul\((\d{1,3}),(\d{1,3})\)',text)
    opc=0
    summation=0
    for operation in operations:        
        summation+=int(operation[0])*int(operation[1])
        opc+=1
    return summation
#print(multiply(text=data))
    

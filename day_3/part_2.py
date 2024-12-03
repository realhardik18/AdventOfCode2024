import re
from part_1 import multiply

with open('input.txt','r') as file:
    data=file.read()

data=data.replace("don't()",'=')
data=data.replace("do()",'_')
dos=re.finditer(r'=',data)
donts=re.finditer(r"_",data)
dc=0
validity=[]
enable=True
for i in data:
    if i=="=":
        enable=False
    elif i=='_':
        enable=True
    validity.append(enable)

summation=0
operations=re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)',data)
for s in operations:
    if validity[s.span()[0]]:
        summation+=multiply(s.group())
    else:
        print(False)
print(summation)



    





    

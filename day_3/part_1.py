import re
with open('input.txt','r') as file:
    data=file.read()

operations=re.findall(r'mul\((\d{1,3}),(\d{1,3})\)',data)
summation=0
for operation in operations:        
    summation+=int(operation[0])*int(operation[1])
print(summation)
    

from checker import issafe
with open('input.txt','r') as file:
    lines=file.readlines()
safe_counter=0
for line in lines:
    level=list(map(int,line.strip().split(' ')))        
    if issafe(level):
        safe_counter+=1
    else:
        print(level)
print(safe_counter)
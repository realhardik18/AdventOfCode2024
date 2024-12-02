with open('input.txt','r') as file:
    lines=file.readlines()
safe_counter=0
for line in lines:
    level=list(map(int,line.strip().split(' ')))    
    valid=True
    #print(sorted(level),level)    
    if sorted(level)==level or sorted(level)==level[::-1]:                                                
        for i in range(1,len(level)):
            if abs(level[i-1]-level[i]) not in [1,2,3]:
                valid=False        
    else:
        valid=False
    if valid:        
        safe_counter+=1
print(safe_counter)
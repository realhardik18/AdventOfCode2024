from helpers import operate

with open('input.txt','r') as file:
    data=list(map(int,file.read().split(' ')))

blinks=6
d=dict()

for x in data:
    d[x]=1
for _ in range(blinks):    
    for num in list(d):        
        count=d[num]   
        d.pop(num)
        y=operate(num)
        if type(y)!=int:
            for number in y:
                if number not in list(d):
                    d[number]=1
                else:
                    d[number]+=count
        else:
            if y not in list(d):
                d[y]=1
            else:
                d[y]+=1
    print(list(filter(lambda x:d[x]>0,d)))
s=0
for i in list(d):
    s=d[i]

            
                








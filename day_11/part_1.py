from helpers import split_number

with open('input.txt','r') as file:
    data=list(map(int,file.read().split(' ')))

blinks=25
outputs=[data]
for _ in range(blinks):
    f=[]
    for num in outputs[-1]:
        if num==0:
            f.append(1)
        elif len(str(num))%2==0:
            f.extend(split_number(num))
        else:
            f.extend([num*2024])
    print(_)
    outputs.append(f)

print(len(outputs[-1]))
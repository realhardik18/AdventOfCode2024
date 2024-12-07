from expression_eval import evaluate_two

with open('input.txt','r') as file:
    data=file.readlines()
    data=[d.strip() for d in data]

def generate_combinations(n, current="", result=None):
    if result is None:
        result = []
    
    if len(current) == n:
        result.append(current)
        return result
    
    generate_combinations(n, current + "*", result)
    generate_combinations(n, current + "+", result)
    generate_combinations(n, current + "|", result)
    return result

summation=0
for index,command in enumerate(data,start=1):
    command=command.split(':')
    command[0]=int(command[0])
    command[1]=list(map(int,command[1].lstrip().split(' ')))    
    ops=generate_combinations(len(command[1])-1)
    outputs=[]
    for op in ops:
        op+='$'
        s=''
        for i,j in zip(command[1],op):
            s+=str(i)+j
        total=0
        for i in s[:-1]:
            total
        outputs.append((s[:-1]))
    
    outputs=[x for x in outputs]        
    print(outputs)
print(summation)
                           
                                                    

    

        






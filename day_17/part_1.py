import numpy as np

with open('input.txt','r') as file:
    d=[l.strip() for l in file.readlines()]

register_a=int(d[0].split(':')[-1])
register_b=int(d[1].split(':')[-1])
register_c=int(d[2].split(':')[-1])

commands=list(map(int,d[-1].split(':')[-1].lstrip().split(',')))
chunks=np.array_split(commands,len(commands)//2)
chunks=[c.tolist() for c in chunks]
print(chunks)
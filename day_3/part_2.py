import re
from part_1 import multiply

enable=True
with open('input.txt','r') as file:
    data=file.read()

operations=re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)',data)
dos=[x.span()[0] for x in re.finditer(r'do\(\)',data)]
donts=[x.span()[0] for x in re.finditer(r"don't\(\)",data)]
dos.insert(0,0)
v1=0
v2=0
ranges=[]
try:
    for _ in range(len(donts)):           
        if dos[v1]<donts[v2]:                 
            ranges.append((dos[v1],donts[v2]))
            v1+=1
            v2+=1
        else:
            while dos[v1]>donts[v2]:
                v2+=1
except Exception as e:
    pass
filtered_ranges=[ranges[0]]
for r in ranges[1:]:
    if filtered_ranges[-1][-1]<r[0]:
        filtered_ranges.append(r)
    else:
        print('hm')
print(filtered_ranges)


    





    

with open('input.txt','r') as file:
    r=file.readlines()
l1=[]
l2=[]
for line in r:
    value=list(map(int,list(line.strip().split('  '))))
    l1.append(value[0])
    l2.append(value[1])
l1.sort()
l2.sort()
total_distance=0
for i in range(len(l1)):
    total_distance+=abs(l1[i]-l2[i])
print(total_distance)

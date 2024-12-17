with open('input.txt','r') as file:
    r=file.readlines()
l1=[]
l2=[]
for line in r:
    value=list(map(int,list(line.strip().split('  '))))
    l1.append(value[0])
    l2.append(value[1])
similarity_score=0
for i in l1:
    similarity_score+=i*l2.count(i)
print(similarity_score)

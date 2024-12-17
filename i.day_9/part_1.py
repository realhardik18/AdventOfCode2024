with open('input.txt','r') as file:
    data=file.read()

s=''
v=0
for index,value in enumerate(data):
    if index%2==0:
        s+=int(value)*str(v)
        v+=1
    else:
        s+='.'*int(value)
print(s)



with open('input.txt','r') as file:
    data=[r.strip() for r in file.readlines()]

size_x,size_y=11,7
#def determine_quadrant()
positions=[]
for row in data:
    position,velocity=row.split(' ')[0][2:].split(','),row.split(' ')[1][2:].split(',')
    position=list(map(int,position))
    velocity=list(map(int,velocity))    
    for i in range(5):
        position[1]+=velocity[1]                
        if position[1]<0:
            position[1]=position[1]+size_y
        position[1]=position[1]%size_y

        position[0]+=velocity[0]                
        if position[0]<0:
            position[0]=position[0]+size_x
        position[0]=position[0]%size_x    

    if position[0]==(size_x-1)//2 or position[1]==(size_y-1)//2:
        pass
    else:
        positions.append(position)
print(len(positions))

with open('input.txt','r') as file:
    data=[r.strip() for r in file.readlines()]

size_x,size_y=101,103
def determine_quadrant(board_lenght,board_height,positions):
    relative_origin=((board_lenght-1)//2,(board_height-1)//2)
    if positions[0]>relative_origin[0] and positions[1]>relative_origin[1]:
        return 1
    elif positions[0]<relative_origin[0] and positions[1]>relative_origin[1]:
        return 2
    elif positions[0]<relative_origin[0] and positions[1]<relative_origin[1]:
        return 3
    else:
        return 4
    
positions=[]
seconds=100
c=[0,0,0,0]
for row in data:
    position,velocity=row.split(' ')[0][2:].split(','),row.split(' ')[1][2:].split(',')
    position=list(map(int,position))
    velocity=list(map(int,velocity)) 

    dist_x=velocity[0]*seconds
    dist_y=velocity[1]*seconds    
    position[0],position[1]=(dist_x+position[0])%size_x,(dist_y+position[1])%size_y
    if position[0]==(size_x-1)//2 or position[1]==(size_y)//2:
        pass
    else:
        c[determine_quadrant(size_x,size_y,position)-1]+=1

print(eval('*'.join(list(map(str,c)))))

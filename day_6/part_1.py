with open('input.txt','r') as file:
    data=file.readlines()
    data=[l.strip() for l in data]

directions={
    '^':0,
    '>':1,
    'v':2,
    '<':3
}

hashes=[]
current_guard_coordinate=[]
guard_coordinates=[]
dir_value=4
exited=False

for y,yd in enumerate(data):
    for x,xd in enumerate(yd):
        if xd=='#':
            hashes.append((x,y))
        if xd in directions.keys():
            current_guard_coordinate=[x,y]
            guard_coordinates.append(current_guard_coordinate)
            dir_value+=directions[xd]

while not exited:
    if dir_value%4==0:
        approchable_hashes=[]
        for hash in hashes:
            if hash[0]==current_guard_coordinate[0] and current_guard_coordinate[1]>hash[1]:
                approchable_hashes.append(hash)
        if len(approchable_hashes)==0:
            exited=True
            current_guard_coordinate=[current_guard_coordinate[0],0]
            guard_coordinates.append(current_guard_coordinate)
        else:
            approchable_hashes.sort(key=lambda hash: hash[1],reverse=True)
            approached_hash=approchable_hashes[0]
            current_guard_coordinate=[current_guard_coordinate[0],approached_hash[1]+1]
            guard_coordinates.append(current_guard_coordinate)
            dir_value+=1

    elif dir_value%4==1:
        approchable_hashes=[]
        for hash in hashes:
            if hash[1]==current_guard_coordinate[1] and current_guard_coordinate[0]<hash[0]:
                approchable_hashes.append(hash)
        if len(approchable_hashes)==0:
            exited=True
            current_guard_coordinate=[len(data[0]),current_guard_coordinate[1]]
            guard_coordinates+=[current_guard_coordinate]        
        else:
            approchable_hashes.sort(key=lambda hash: hash[0])
            approached_hash=approchable_hashes[0]
            current_guard_coordinate=[approached_hash[0]-1,current_guard_coordinate[1]]
            guard_coordinates.append(current_guard_coordinate)
            dir_value+=1
        
    elif dir_value%4==2:
        approchable_hashes=[]
        for hash in hashes:
            if hash[0]==current_guard_coordinate[0] and current_guard_coordinate[1]<hash[1]:
                approchable_hashes.append(hash)
        if len(approchable_hashes)==0:
            exited=True
            current_guard_coordinate=[current_guard_coordinate[0],len(data)]
            guard_coordinates.append(current_guard_coordinate)
        else:
            approchable_hashes.sort(key=lambda hash: hash[1])
            approached_hash=approchable_hashes[0]
            current_guard_coordinate=[current_guard_coordinate[0],approached_hash[1]-1]
            guard_coordinates.append(current_guard_coordinate)
            dir_value+=1

    elif dir_value%4==3:
        approchable_hashes=[]
        for hash in hashes:
            if hash[1]==current_guard_coordinate[1] and current_guard_coordinate[0]>hash[0]:
                approchable_hashes.append(hash)
        if len(approchable_hashes)==0:
            exited=True
            current_guard_coordinate=[0,current_guard_coordinate[1]]
            guard_coordinates.append(current_guard_coordinate)
        else:
            approchable_hashes.sort(key=lambda hash: hash[0],reverse=True)
            approached_hash=approchable_hashes[0]
            current_guard_coordinate=[approached_hash[0]+1,current_guard_coordinate[1]]
            guard_coordinates.append(current_guard_coordinate)
            dir_value+=1


#print(exited)
covered_coordinates=set()
for index,coordinate in enumerate(guard_coordinates[:-1]):
    if guard_coordinates[index][0]==guard_coordinates[index+1][0]:
        thresholds=[guard_coordinates[index][1],guard_coordinates[index+1][1]]
        for y in range(min(thresholds),max(thresholds)+1):
            covered_coordinates.add((guard_coordinates[index][0],y))
    else:
        thresholds=[guard_coordinates[index][0],guard_coordinates[index+1][0]]
        for x in range(min(thresholds),max(thresholds)+1):
            covered_coordinates.add((x,guard_coordinates[index][1]))        

print(len(covered_coordinates))



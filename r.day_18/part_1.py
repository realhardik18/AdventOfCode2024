with open('input.txt','r') as file:
    bad_locations=[tuple(map(int,d.strip().split(','))) for d in file.readlines()]

grid_size=6
good_loactions=[]
for i in range(grid_size):
    for j in range(grid_size):
        if (i,j) in bad_locations:
            pass
        else:
            good_loactions.append((i,j))
print(good_loactions)


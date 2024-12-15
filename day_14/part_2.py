from PIL import Image

with open('input.txt','r') as file:
    data=[r.strip() for r in file.readlines()]

size_x,size_y=101,103

def plot_map(filename, coords):        
    img = Image.new("RGB", (size_x, size_y), "red")
    pixels = img.load()        
    for x, y in coords:
        if 1 <= x <= size_x and 1 <= y <= size_y:
            pixels[x - 1, size_y - y] = (255, 255, 255) 
    img.save(f"maps/{filename}.png")
    
positions=[]
seconds=10000
for second in range(seconds):
    positions_per_second=[]
    for row in data:
        position,velocity=row.split(' ')[0][2:].split(','),row.split(' ')[1][2:].split(',')
        position=list(map(int,position))
        velocity=list(map(int,velocity)) 

        dist_x=velocity[0]*second
        dist_y=velocity[1]*second
        position[0],position[1]=(dist_x+position[0])%size_x,(dist_y+position[1])%size_y                            
        positions_per_second.append(tuple(position))
    plot_map(str(second),positions_per_second) 
    print(f"plotted for {second}")                                       

with open('input.txt','r') as file:
    data=file.readlines()
    data=[list(row.strip()) for row in data]

#size = (width,lenght)
size = (len(data[0]),len(data))    
c=0
for row_number,row in enumerate(data):
    for index,letter in enumerate(row):
        if letter=='A': 
            if row_number-1>=0 and row_number+1<=size[0]-1 and index-1>=0 and index+1<=size[0]-1:
                if ''.join(sorted([data[row_number-1][index-1],'A',data[row_number+1][index+1]]))=='AMS' and ''.join(sorted([data[row_number-1][index+1],'A',data[row_number+1][index-1]]))=='AMS':                    
                    c+=1
print(c)
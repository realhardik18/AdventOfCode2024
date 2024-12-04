import re
import numpy as np

with open('input.txt','r') as file:
    data=file.readlines()
    data=[list(row.strip()) for row in data]

#size = (width,lenght)
size = (len(data[0]),len(data))    

horizontal_count=0
vertical_count=0
diaganol_upper_right_count=0
diaganol_upper_left_count=0
diaganol_lower_right_count=0
diaganol_lower_left_count=0

#to check for hortizontally forwards and backwards
for row in data:
    results=re.findall(r'XMAS',''.join(row))
    results_reverse=re.findall(r'XMAS',''.join(row[::-1]))
    horizontal_count+=len(results)
    horizontal_count+=len(results_reverse)

#to check for vertically forward and backwards
transpose_matrix=np.matrix(data).T
for row in transpose_matrix:
    r=np.ndarray.tolist(row)[0]
    results=re.findall(r'XMAS',''.join(r))
    results_reverse=re.findall(r'XMAS',''.join(r[::-1]))
    vertical_count+=len(results)
    vertical_count+=len(results_reverse)    
#print(vertical_count,horizontal_count)

#to check for vertically upwards towards the right
for row_number,row in enumerate(data):
    for index,letter in enumerate(row):
        if letter=='X':            
            if index+3<=size[0]-1 and row_number-3>=0:
                sub_string=''
                for i in range(4):
                    sub_string+=data[row_number-i][index+i]
                if sub_string=='XMAS':                    
                    diaganol_upper_right_count+=1
            else:
                pass
        else:
            pass

#to check for vertically upwards towards the left
for row_number,row in enumerate(data):
    for index,letter in enumerate(row):
        if letter=='X':            
            if index-3>=0 and row_number-3>=0:
                sub_string=''
                for i in range(4):
                    sub_string+=data[row_number-i][index-i]                
                if sub_string=='XMAS':                    
                    diaganol_upper_left_count+=1
            else:
                pass
        else:
            pass

#to check vertically downwards towards the right
for row_number,row in enumerate(data):
    for index,letter in enumerate(row):
        if letter=='X':            
            if index+3<=size[0]-1 and row_number+3<=size[0]-1:
                sub_string=''
                for i in range(4):
                    sub_string+=data[row_number+i][index+i]                
                if sub_string=='XMAS':                    
                    diaganol_lower_right_count+=1
            else:
                pass
        else:
            pass

#to check vertically downwards towards the left
for row_number,row in enumerate(data):
    for index,letter in enumerate(row):
        if letter=='X':            
            if index-3>=0 and row_number+3<=size[0]-1:
                sub_string=''
                for i in range(4):
                    sub_string+=data[row_number+i][index-i]                
                if sub_string=='XMAS':                    
                    diaganol_lower_left_count+=1
            else:
                pass
        else:
            pass        

counts=[
    horizontal_count,
    vertical_count,
    diaganol_lower_left_count,
    diaganol_lower_right_count,
    diaganol_upper_left_count,
    diaganol_upper_right_count
]
print(sum(counts))
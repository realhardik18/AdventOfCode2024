import re
import numpy as np

with open('input.txt','r') as file:
    data=file.readlines()
    data=[list(row.strip()) for row in data]

#size = (width,lenght)
size = (len(data[0]),len(data))    

horizontal_count=0
vertical_count=0

#to check for hortizontally forwards and backwards
for row in data:
    results=re.findall(r'XMAS',''.join(row))
    results_reverse=re.findall(r'XMAS',''.join(row[::-1]))
    horizontal_count+=len(results)
    horizontal_count+=len(results_reverse)

transpose_matrix=np.matrix_transpose(np.matrix(data))
for row in transpose_matrix:
    r=np.ndarray.tolist(row)[0]
    results=re.findall(r'XMAS',''.join(r))
    results_reverse=re.findall(r'XMAS',''.join(r[::-1]))
    vertical_count+=len(results)
    vertical_count+=len(results_reverse)    
print(vertical_count,horizontal_count)

#print(horizontal_count)


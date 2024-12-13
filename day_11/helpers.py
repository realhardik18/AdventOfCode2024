def split_number(n):
    n=str(n)
    l=len(n)
    part_1=int(n[:l//2])
    part_2=int(n[l//2:])
    return [part_1,part_2]

def operate(n):
    if len(str(n))%2==0:
        return split_number(n)
    elif n==0:
        return 1
    else:
        return 2024*n

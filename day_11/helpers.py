def split_number(n):
    n=str(n)
    l=len(n)
    part_1=int(n[:l//2])
    part_2=int(n[l//2:])
    return [part_1,part_2]

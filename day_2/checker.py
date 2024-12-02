def issafe(array):
    valid=True
    if sorted(array)==array or sorted(array)==array[::-1]:
        for i in range(1,len(array)):
            if abs(array[i-1]-array[i]) not in [1,2,3]:
                return False
        return True
    else:
        return False    
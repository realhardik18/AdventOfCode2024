with open('input.txt','r') as file:
    data=[x.strip() for x in file.readlines()]

directions={
    '^':0,
    '>':1,
    'v':2,
    '<':3
}


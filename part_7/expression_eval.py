def evaluate(string):
    nums=[]
    exp=[]
    tn=''
    total=None
    for s in string:
        if s=='+':
            if total==None:    
                total=int(tn)
            else:
                total=eval(f'total{exp[-1]}{tn}')
            nums.append(tn)
            exp.append('+')                                
            tn=''
        elif s=='*':
            if total==None:    
                total=int(tn)
            else:
                total=eval(f'total{exp[-1]}{tn}')
            nums.append(tn)
            exp.append('*')                                
            tn=''            
        else:
            tn+=s
    total=eval(f'total{exp[-1]}{tn}')
    return total
#print(evaluate('10*19'))
#['81*40*27', '81*40+27', '81+40*27', '81+40+27']
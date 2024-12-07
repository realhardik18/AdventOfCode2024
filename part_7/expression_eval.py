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
    print(f'hiiiiiiiiii{len(exp)}')
    return total

def evaluate_two(string):
    if '|' in string:
        data=[]
        exp=[]
        tn=''
        total=None
        for s in string:
            if s=='+':
                data.append(tn)
                data.append('+')                                            
                tn=''
            elif s=='*':
                data.append(tn)
                data.append('*')                                            
                tn=''
            elif s=='|':
                data.append(tn)
                data.append('|')                                                            
                tn=''
            else:
                tn+=s
        data.append(tn)
        conc_ind=data.index('|')
        simplified=data[conc_ind-1]+data[conc_ind+1]
        m=''.join(simplified)
        #print(m)    
        prev=str(evaluate(data[:conc_ind]))+str(data[conc_ind+1])                
        print(evaluate(str(prev)+''.join((data[conc_ind+2:]))))
    else:
        print(string,'@')
        return evaluate(string)
print(evaluate_two('8|6'))
#['81*40*27', '81*40+27', '81+40*27', '81+40+27']
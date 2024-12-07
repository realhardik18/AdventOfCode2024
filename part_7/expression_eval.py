def evaluate(string):
    nums=[]
    exp=[]
    tn=''
    total=None    
    if '+' not in string and '*' not in string:
        return string
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
    return int(total)

def evaluate_two(string):
    if '|' in string:        
        data=[]        
        tn=''        
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
        #print(evaluate(''.join(data[:conc_ind])))
        simplified=str(evaluate(''.join(data[:conc_ind])))+data[conc_ind+1]
        return evaluate(simplified+''.join(data[conc_ind+2:]))
    else:    
        return evaluate(string)

print(evaluate_two('4|4|4'))
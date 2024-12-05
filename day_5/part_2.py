with open('orders.txt','r') as file:
    orders=[o.strip() for o in file.readlines()]
with open('updates.txt','r') as file:
    updates=file.readlines()
summation=0
for update in updates:
    unverfied_orders=update.strip().split(',')
    #print(unverfied_orders)
    verified_update=True
    for i in range(len(unverfied_orders)-1):
        unverified_order=unverfied_orders[i]+'|'+unverfied_orders[i+1]
        if unverified_order not in orders:
            verified_update=False
            break
    if not verified_update:        
        for j in range(len(unverfied_orders)-1):
            for i in range(len(unverfied_orders)-1):
                if unverfied_orders[i]+'|'+unverfied_orders[i+1] not in orders:
                    unverfied_orders[i],unverfied_orders[i+1]=unverfied_orders[i+1],unverfied_orders[i]
        summation+=int(unverfied_orders[(len(unverfied_orders)-1)//2])
print(summation)





                

    
        

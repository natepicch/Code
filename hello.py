def cap(name): 
    i = 0 
    a = '' 
    b = [] 
    while i != len(name):
        if i == 0 or i == 3:
            b.append(name[i].upper())
        else: 
            b.append(name[i].lower()) 
        i+=1 
        
    return a.join(b)

#lesseroftwo
def lesser_of_the_two(a,b):
    if a%2 == 0 and b%2 == 0 and a < b: 
        return a
    else: 
        return b

#makeinputletter1and4cap
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
#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere
def ints(input):
    for i in range(0,len(input)-1): #goes up to len(input)-1 becauseif it went to the end it would compare the last number with i+1 being nothing
        if i == 3 and i + 1 == 3:
            return 'True'
        else:
            return 'False'

#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
 def triple(string):
     a = ''
     for char in string:
         a = a + char*3 
    return a

    


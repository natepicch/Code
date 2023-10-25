#Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase. 
def myfunc(opposite):
    i = ran
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
     for char in string: #takes each interable for the string put into the function and stores it in char 1 by 1
         a = a + char*3 
    return a

#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def guess(a,b,c):
    if a + b + c <= 21:
        return a + b + c
    elif a + b + c > 21 and a == 11 or b ==11 or c == 11:
        return a + b + c - 11 
    elif a + b + c > 21:
        return "BUST"
    
    
    

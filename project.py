import random

def gameWin(comp,you):
    #if two values are equal, declare a tie!
    if comp==you:
        return None
        #check for all posibility when computer chose s
    if comp=='s':
        if you=='w':
            return False
        elif  you=='g':
            return True   
     #check for all posibility when computer chose w
    if comp=='w':
        if you=='g':
            return False
        elif  you=='s':
            return True    
     #check for all posibility when computer chose g  
    if comp=='g':
        if you=='s':
            return False
        elif  you=='w':
            return True              
print("Comp turn : Snake(s) water(w) or gun(g)?")    
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'    
else:
    comp='g'
you=input("your turn : Snake(s) water(w) or gun(g)?")

a=gameWin(comp,you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a==None:
    print("The game is tie! ")
elif a :
    print("You win ")
else:
    print("You loose")    

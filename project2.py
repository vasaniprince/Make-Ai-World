import random
randNumber=random.randint(1,100)
userGuess=None
guesses=0
while(userGuess!=randNumber):
    userGuess=int(input("Enter your guess : "))
    guesses+=1 
    if(userGuess==randNumber):
        print("You are right")
    # elif(userGuess<randNumber):
    #     print("Enter the Big Number")
    else:
         if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller Number") 
         else:
            print("You guessed it wrong! Enter a larger Number")   

print(f"you guessed in {guesses} gusses") 
with open("highscore.txt","r") as f:
    highscore=int(f.read())  

if(guesses<highscore):   
    print("You just broken the highscore")   
    with open("highscore.txt" , "w") as f:
         f.write(str(guesses))
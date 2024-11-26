import random

options = ["rock" , "paper", "sissors"]
 
userwins = 0
computerwins = 0

while True:
    userinput = input("Enter your choice  or  Press Q to quit -  ").lower
    if userinput == "q":
        break
    if userinput == options:
        continue
    
    randomnumber = random.randint(0, 2)
    computerchoice = options[randomnumber]
    print(computerchoice)  
    
    if userinput == "rock" and computerchoice == "sissors":
        print("You win ")
        userwins += 1
    elif userinput == "paper" and computerchoice == "rock":
        print("You Win ")
        userwins += 1
    elif userinput == "sissors" and computerchoice == "paper":
        print("You Win ")
        userwins += 1
    else:
        print("You Lose ")
        computerwins += 1
        
      
    print("You Won ", userwins, "Times") 
    print("You Lost ", computerwins, "Times to the computer")   
    print("Thank you for playing ")
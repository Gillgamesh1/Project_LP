print("Wellcome to KBC")
playing = input("Do you want to play KBC ?  ")
if playing != "yes":
    quit()
print("Good lets play KBC !!!")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!!!")
    score += 1
else:print("Incorrct")



answer = input("What is the capital of India? ")
if answer.lower() == "new delhi":
    print("Correct !!!")
    score += 1
else:print("Incorret")


answer = input("What is the capital of Maharashtra? ")
if answer.lower() == "mumbai":
    print("Correct !!!")
    score += 1
else:print("Incorrect")


print("Your final score is  " + str(score) )
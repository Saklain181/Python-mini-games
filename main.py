import random
scores={"user":0,"computer":0}
u=["stone","paper","scissors"]
while True:
    user=input("Enter your choice (stone, paper, scissors): ")
    if user in u:
        computer=random.choice(u)
        print("Computer's choice:", computer)
        if user==computer:
            print("It's a tie!")
        elif (user=="stone" and computer=="scissors") or (user=="paper" and computer=="stone") or (user=="scissors" and computer=="paper"):
            print("You win!")
            scores["user"]+=1
        else:
            print("Computer wins!")
            scores["computer"]+=1

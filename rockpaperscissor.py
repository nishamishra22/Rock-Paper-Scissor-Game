import random

def Game(comp,you):
    if comp==you:
        return None
    
    elif comp=='r':
        if you=='p':
            return True
        elif you=='s':
            return False
        
    elif comp=='p':
        if you=='r':
            return False
        elif you=='s':
            return True
        
    elif comp=='s':
        if you=='p':
            return False
        elif you=='r':
            return True
    
i=1
f=True
while(i<=2):
    print("Press 1 to play")
    print("press 2 to exit")
    v=int(input("Enter Your choice: "))
    if v==1:
        f=True
    elif v==2:
        f=False
    else:
        print("wrong choice..")
        exit()

    if f:    
        print("Computer's turn: Rock(r),Paper(p),Scissor(s)?")
        num=random.randint(1,3)
        if num==1:
            comp='r'
        elif num==2:
            comp='p'
        else:
            comp='s'

        you = input("Your Turn: Rock(r),Paper(p),Scissor(s)?")
        n=Game(comp,you)

        print(f"Computer chose {comp}")
        print(f"You chose {you}")

        if n==None:
            print("The game is a Tie!!")
        elif n:
            print("You Win!!")
        else:
            print("You Lose!!")

    else:
        print("Thank you for playing..")
        exit()
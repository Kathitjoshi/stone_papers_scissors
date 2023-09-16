import random
import time
i=0
x=0
y=0

print("Welcome to rock,paper and scissors game!!!")
print("1----Stone")
print("2----Paper")
print("3----Scissors")
while(i<=1) :
    if i%2==0 :
        print("It is the first player's chance")
        x=random.randint(1,3)
        if x==1:
            print("first player chose stone")
        elif x==2 :
            print("first player chose paper")
        else :
            print("first player chose scissors")
        time.sleep(2)
    else :
        print("It is the second player's chance")
        y=random.randint(1,3)
        if y==1:
            print("second player chose stone")
        elif y==2 :
            print("second player chose paper")
        else :
            print("second player chose scissors")
        time.sleep(2)
    i=i+1
if (x==y) :
    print("tie game")
elif(x==1 and y==2):
    print("second player won the game as paper beats stone")
elif(x==1 and y==3):
    print("first player won the game as stone beats scissors")
elif(x==2 and y==1):
    print("first player won the game as paper beats stone")
elif(x==2 and y==3):
    print("second player won the game as scissors beats paper")
elif(x==3 and y==1):
    print("second player won the game as stone beats scissors")
else :
    print("first player won the game as scissors beats paper")
    
    
    
    

    
        
              

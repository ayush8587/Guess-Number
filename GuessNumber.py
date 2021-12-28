n=5
print("You have",n,"Chances to Guess the Correct Number")
while(n!=0):
    inp = int(input("Enter the number:"))
    if inp==18:
        print("Hurray!!!! You Guess the correct number!!!")
        break
    elif (inp<18) and (inp>15):
        print("You are very close to the correct number,But it is lesser than the correct number")
    elif (inp>18) and (inp<20):
        print("You are very close to the correct number,But it is greater than the correct number")
    elif (inp>=20) and (inp<30):
        print("You are close to the correct number,but it is greater than the correct number")
    elif inp>=30:
        print("Entered number is greater than the correct number")
    elif (inp<=15) and (inp>10):
        print("You are close to the correct number,but it is lesser than the correct number")
    elif inp<=10:
        print("Entered number is lesser than the correct number")
    else:
        print("You are very far to the correct number,Please Try Again!!!")
    n=n-1
    print(n,"Chances left")
    if(n==0):
        print("Game Over , You lost")
        break
import random
guess=5
secret_no=random.randint(1,101)
n=1
guess=int(input("enter the no: "))
while guess!=secret_no:
    if secret_no<guess:
        print("no is less than ",guess)
    elif secret_no>guess:
        print("no is greater than ",guess)
    n=n+1
    guess=int(input("enter the no: "))
    
print("yes! you are right")
print("you took chance:",n )


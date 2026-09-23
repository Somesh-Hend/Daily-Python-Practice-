#Basic Practice of python
print("Wellcome To Last Challage".center(65))
print("This is on your gussing completly".center(65))
input("Click Enter To start last challage")
print("You having 5 doors select any one")
a=input("Write Your Option:")
if a=="1" or a=="2" or a=="3":
    print("You are catch in trap")
    print("GAME OVER")
elif a=="4" or a=="5":
    print("YOU WIN !!!!!!")
else:
    print("Time Out You lose")
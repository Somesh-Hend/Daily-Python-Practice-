print("----Wellcome To Tikit Conform Website----".center(65))
name=input("Tell Your Name:")
print("Wellcome",name,"!!!!")
age=int(input("Tell whats your actual Age:"))

if age<=15:
    print("You are not eligibel for Game")
    print("You are ",age," year old only")
    a=15-age
    print("After your",a, "Birthday you are eligibal for game")
    exit( )
else:
    print("You are Pass first test")
print("Now Tell Mi do you have any heart problem")
g=input("Yes or No:")
if g=="Yes":
    print("Unfortunatly You are not eligibal for game")
elif g=="no":
    print("Congrast, you are playing with kamla")
else:
    print("chose correct option")
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
if g=="yes":
    print("Unfortunatly You are not eligibal for game")
elif g=="no":
    print("Congrast, you are playing with kamla")
else:
    print("chose correct option")
    exit( )
input("Book Your Slot Now!!!")
c=int(input("Enter what difficalty level you want 1 to 10:"))

if c<= 2:
    print("You chose easy level Your code is A")
    print("you having 2 times of your dificalty mode")
elif c<= 4:
    print("You chose medium level Your code is B")
    print("You having 2 times of your dificalty mode")
elif c<=6:
    print("You chose Hard level Your code is C")
    print("You having 2 times of your dificalty mode")
elif c<=8:
    print("You chose extream level Your code is D")
    print("You have only 1 time in a day")
elif c<=10:
    print("You chose Imposibal mode Your code is E")
    print("You having rearly one in a day")
else:
    print("Chose correct Level Of difficalty")
    exit( )
def payment_page( ):
    global payment
    global z
    if payment==z:
        print("Your payment is sucesfull")
        print("Congrajulation !!!!! Your slot is booked")
    else:
        print("Transection canceled")
print("--------Important anounsment--------".center(66))
print("You Have To make only UPI payments".center(65))
a=input("Enter Your slot code to get slot:")
if a=="A":
    print("Wellcome to Payment page")
    print('pay \'1500.rs\' For this mode')
    z=1500
    payment=int(input("Enter Your Amount:"))
    payment_page( )
elif a=="B":
    print("Wellcome to payment page")
    print("pay \"1700.rs\" For this mode")
    z=1700
    payment=int(input("Enter Your Amount:"))
    payment_page( )
elif a=="C":
    print("Wellcome to payment page")
    print("pay \"2000.rs\" For this mode")
    z=2000
    payment=int(input("Enter Your Amount:"))
    payment_page( )
elif a=="D":
    print("Wellcome to payment page")
    print("pay \"2200.rs\" For this mode")
    z=2200
    payment=int(input("Enter Your Amount:"))
    payment_page( )
elif a=="E":
    print("Wellcome to payment page")
    print("pay \"2500.rs\" For this mode")
    z=2500
    payment=int(input("Enter Your Amount:"))
    payment_page( )
else:
    print("Enter correct code")
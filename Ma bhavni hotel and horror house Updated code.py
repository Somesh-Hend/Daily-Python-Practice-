#Ma bhavni hotel and horror house Updated code
name=input("Enter Your Name:")
print(f"Welcome {name}!!!! To Ma Bhavni Restorent & Horror House")
print("About Us:")
print("Welcome To Our website we are giving pepeals real life horror Experienses")
input("click enter")
def members( ):
    global member
    if member>=5:
        print("You Have To book small table")
    else:
        print("We have to sort you in grups")
print("Whats You Like to Expirience First")
print("Enter R for restorent expirience Enter H for horror House expirience")
option=input("Whats Your have To expireance:")
if option=='r' or option=='R':
    print(f"Welcome {name} You selected our very primium section")
    print("Book Your Table Now!!!!!")
    member=int(input("Enter Number of Members:"))
    tabletype=input("Enter Which type of table would you have Normal/Gaming Airdrop/Gaming charging:")
    if tabletype=="Normal" or tabletype=="Gaming Airdrop" or tabletype=="Gaming Charging":
        members( )
elif option=="H" or option=="h":
    print(f"Welcome {name} To our primium gaming section")
    print("Coming soon.....")
else:
    print("Somthing went wrong")
 
print("Wellcome to somesh system".center(60))
print("-----------------------------------------------------------------")
name=input("Enter Your Name:")
email=input("Enter Your Email:")
passward=input("Enter the strong passward:")
print("Wellcome",name,"!!!")
print("reenter your information")
input("click enter")
mail=input("Reenter the email:")
if email==mail:
    print("your email is correct,Now enter the passward")
    passwar=input("Enter the correct passward:")
    if passward==passwar:
        print("Wellcome Back",name)
    else:
        print("Enter the correct passward")
else:
    print("enter the correct email")
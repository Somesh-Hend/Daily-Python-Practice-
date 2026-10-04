#Som Oprating System
name=input("Enter Your name:")
email=input("Enter Your email:")
if "@" in email:
    print("Enter The Mix Passward of 6letters")
    passward=input("Enter Your Passward:")
    le=len(passward)
    pas=passward.isalnum( )
    if le==6 and pas==True:
        print(f"Wellcome To oprating system {name}")
    else:
       print("Something went wrong")       
else:
    print("Enter correct Email")
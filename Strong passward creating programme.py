#Strong passward creating programme
print("Enter Mix Passward")
password = input("Enter Your Password: ")

if password.isalnum():
    print("Valid Password! (Contains only letters and numbers)")
else:
    print("Invalid Password! (Special characters not allowed)")

#Orthagonal Matrix Find in 2×2
print("[A     B]")
print("[C     D]")
a=int(input("A:"))
b=int(input("B:"))
c=int(input("C:"))
d=int(input("D:"))
print("conform your matrix")
print(f"[{a}     {b}]")
print(f"[{c}     {d}]")
z=input("For Finding determinant enter b:")
if z=="b":
    u=(a*d)-(b*c)
    print(u)
else:
    print("Somthing Went wrong")
input("click enter to find invers")
print("Your matrix invers is")
print(f"[{d}/{u}    {b}/{-u}]")
print(f"[{c}/{-u}    {a}/{u}]")
s1=d/u   
s2=b/-u
s3=c/-u
s4=a/u
input("Want To Find Is it orthagonal or not click Enter")
print("First We want to find Transpose of matrix Transpose of matrix is")
print(f"{a}     {c}")
print(f"{b}     {d}")
s5=a
s6=c
s7=b
s8=d
if s1==s5 and s2==s6 and s3==s7 and s4==s8:
    print("It's Orthagonal Matrix")
else:
    print("Not Orthagonal Matrix")
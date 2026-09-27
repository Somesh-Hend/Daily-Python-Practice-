#2×2 matrix solution finding program
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
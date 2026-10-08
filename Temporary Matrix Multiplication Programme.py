#Matrix Multiplication Programme
input("Wellcome To Matrix Multiplication Programme")
print("Enter In 2×2,3×3")
def infotakingfortwo():
    global i1,i2,i3,i4,i5,i6,i7,i8
    i1=int(input("Enter A:"))
    i2=int(input("Enter B:"))
    i3=int(input('Enter C:'))
    i4=int(input("Enter D:"))
    print(f"[{i1}    {i2}]")
    print(f"[{i3}    {i4}]")
    i5=int(input("Enter E:"))
    i6=int(input("Enter F:"))
    i7=int(input("Enter G:"))
    i8=int(input("Enter I:"))
    print(f"[{i5}    {i6}]")
    print(f"[{i7}    {i8}]")
def multiplicationfirst( ):
    global i1,i2,i3,i4,i5,i6,i7,i8
    global a11,a22,a12,a21
    a11=(i1*i5)+(i2*i7)
    a12=(i1*i6)+(i2*i8)
    a21=(i3*i5)+(i4*i7)
    a22=(i3*i6)+(i4*i8)
type=input("Enter What Type Of Matrix Multiplication You need:")
if type=="2×2":
    infotakingfortwo()
    print("Hear 2×2 matrix")
    print(f"[{i1}    {i2}]  [{i5}    {i6}]")
    print(f"[{i3}    {i4}]  [{i7}    {i8}]")
    multiplicationfirst( )
    print(f"[{a11}    {a12}]")
    print(f"[{a21}    {a22}]")
elif type=="3×3":
    print("Hear 3×3 matrix")
else:
    print("Something Went Wrong")
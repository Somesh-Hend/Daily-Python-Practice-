#3×3 matrix determinant finding programme
print("[A   B   C]")
print("[D   E   F]")
print("[G   H   I]")
Z=("A","B","C","D","E","F","G","H","I")
for j in Z:
    globals( )[j]=int(input(f"{j}:"))
print("Conform your 3×3 matrix")
print(f"[{A}   {B}   {C}]")
print(f"[{D}   {E}   {F}]")
print(f"[{G}   {H}   {I}]")
o=input("To get determinant enter \"k\":")
if o=="k":
    l=(E*I)-(F*H)
    op=l*A
    m=(D*I)-(F*G)
    ot=m*B
    n=(D*H)-(E*G)
    oi=n*C
    p=op-ot+oi
    print(p)
else:
    print("Something gets wrong")
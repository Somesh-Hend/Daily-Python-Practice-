#3×3 invers finding program
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
input("click enter to get invers")
num1=(E*I)-(F*H)
num2=(D*I)-(F*G)
num3=(D*H)-(E*G)
num4=(B*I)-(C*H)
num5=(A*I)-(C*G)
num6=(A*H)-(B*G)
num7=(B*F)-(E*C)
num8=(A*F)-(D*C)
num9=(A*E)-(B*D)
print(f"[{num1}/{p}     {num4}/{-p}    {num7}/{p}]")
print(f"[{num2}/{-p}    {num5}/{p}    {num8}/{-p}]")
print(f"[{num3}/{p}    {num6}/{-p}    {num9}/{p}]")
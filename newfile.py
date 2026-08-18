number=int(input("Enter First Number:"))
num=int(input("Enter Secound Number:"))
sign=input("Enter A sign:")

if sign=="+":
    addition=number+num
    print(addition)
elif sign=="-":
    substraction=number-num
    print(substraction)
elif sign=="×":
    multiplication=number*num
    print(multiplication)
elif sign=="÷":
    dividation=number/num
    print(dividation)
else:
    print("Enter correct symbol2")
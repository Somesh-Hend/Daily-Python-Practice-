#leap year identyfrie programme
print("Wellcome To leap year finding programme")
input("click enter")
year=int(input("Enter Year That You Want To Know:"))
z=year%400
s=year%100
y=year%4
if (y==0) and (s!=0) or z==0:
    print("It is an leap Year")
else:
    print("Its not leap year")
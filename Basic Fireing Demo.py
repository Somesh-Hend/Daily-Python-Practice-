#Basic Fireing Demo
def fireing( ):
    global ZHP
    while ZHP>=0:
        print("FIREING....FIREING....")
        input("Clike Enter To fire")
        ZHP=ZHP-26
        print("Zombie Is Dead")
    print("Congrajulation You Won")
ZHP=200
print("Zombie Is coming")
input("Click Enter To Pick Up Gun")
input("Click Enter To fire")
fireing( )
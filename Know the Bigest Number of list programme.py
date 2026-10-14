#Know the Bigest Number of list programme
print("Tell me how many numbers have to check you")
list1=[]
num=int(input("Tell How Many:"))
while num>0:
    number_list=int(input("Enter Number:"))
    list1.append(number_list)
    num=num-1
list1.sort()
print(list1)
print(list1[-1])
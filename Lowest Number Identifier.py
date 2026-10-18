#Lowest Number Identifier
number_list=int(input("Enter How many numbers in your List:"))
list1=[]
while number_list>0:
    numbers=int(input("Enter Number:"))
    list1.append(numbers)
    number_list=number_list-1
list1.sort()
print(list1[0])
# Number Palindrome Checker
number = int(input("Enter a number: "))
original_num = number
reversed_num = 0
while number > 0:
    remainder = number % 10
    reversed_num = (reversed_num * 10) + remainder
    number = number // 10
if original_num == reversed_num:
    print(f"{original_num} is a Palindrome Number!")
else:
    print(f"{original_num} is NOT a Palindrome Number.")
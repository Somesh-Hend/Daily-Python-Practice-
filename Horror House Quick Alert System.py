# Horror House Quick Alert System
visitor_name = input("Enter your name: ")
status = input("Do you dare to enter tonight? (yes/no): ").strip().lower()

if status == "yes":
    print(f"Welcome {visitor_name}! Get ready for the thrill.")
else:
    print(f"Safe choice {visitor_name}! Enjoy your food at the restaurant.")

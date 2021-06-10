# x = 0
#
# while x < 10:
#     print(f"it's working -> {x}")
#     if x == 4:
#         break
#     x += 1

# while True:
#     age = input("What is your age? ")
#     if age == "25":
#         print(f"Correct age entered!")
#         break
#     else:
#         print(f"Incorrect age entered!")

# While Cinema Ticket

def print_ticket():
    while True:
        print("**********Welcome To The Milano Theatre**********")
        age = input("Enter your age to check for ticket price: ")
        while not age.isdigit():
            age = input("Invalid input! Enter your age to check for ticket price: ")
        age = int(age)
        if age < 3:
            print("Your tickets are free!")
        elif 3 <= age <= 12:
            print("The cost of the ticket is £10")
        elif 13 <= age <= 90:
            print("The cost of the ticket is £15")
        else:
            print("Sorry, exceeding age limits..")
        generate_more = input("Do you want to generate more tickets? (Yes/No): ")
        generate_more = generate_more.upper()

        while generate_more != "YES" and generate_more != "Y" and generate_more != "NO" and generate_more != "N":
            generate_more = str(input("Invalid response! Do you want to generate more tickets? (Yes/No): ")).upper()
        if generate_more == "NO" or generate_more == "N":
            print("Goodbye...!")
            break


print_ticket()

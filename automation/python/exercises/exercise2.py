lname = input("Enter your last name: ")
fname = input("Enter your first name: ")
gender = input("what is your gender Y-Male/N-Female?")
if gender == "Y" or gender == "y":
    print("Hello Mr.", fname, lname)
else:
    print("Hello Ms.", fname, lname)


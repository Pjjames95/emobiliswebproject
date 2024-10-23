def concert_program(age):
    if age < 18:
        print("No entry")
    elif 18 <= age <=25:
        print("Free drinks")
    else:
        print("Extra ticket")

age =int(input("Enter your age:"))
concert_program(age)

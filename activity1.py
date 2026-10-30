try:
    number = int(input("Entera number: "))
    print("The number entered is", number)

except ValueError as ex:
    print("Exception:", ex)
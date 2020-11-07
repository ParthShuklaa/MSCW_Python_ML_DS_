import sys


no1 = int(input("Enter first no"))
no2 = int(input("Enter Second no"))
try:
    output = int(no1/no2)
    print(type(no1))
    print(type(no2))
    print(output)
    print(type(output))
    print("Final Output is "+ str(output))
    print(Name)

except ZeroDivisionError:
    print("Do not try to divide a no by 0 ")
    error = sys.exc_info()[0]
    print(error)
    sys.exit()
except NameError:
    print("Define All Variables before using it ")
    error = sys.exc_info()[0]
    print(error)


finally:
    print("Thank you for using my application")

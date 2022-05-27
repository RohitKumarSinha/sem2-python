def celToFah(num):
    temp = 9/5 * num + 32
    print("your number after converting fahrenheit to celsius  ", temp)


def feetToinch(num):
    inch = num * 12
    print("inch of your number is ", inch)


def kiloTopound(num):
    pound = num * 2.205
    print("pound of your kilogram is ", pound)

def metTocm(num):
    cm = num * 100
    print("centimeter of yor meter is ", cm)


num = eval(input("Enter your number :- "))
celToFah(num)
feetToinch(num)
kiloTopound(num)
metTocm(num)

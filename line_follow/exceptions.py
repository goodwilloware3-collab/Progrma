x=10
try:
    if type(x) is not str:
        raise TypeError("x is not a string.")
except ZeroDivisionError:
    print("numbers cannot be divided by zero.")
except NameError:
    print("Variable x is not defined.")
except Exception as error:
    print(error)
else:
    print("Division performed successfully.")
finally:
    print("We did it!")
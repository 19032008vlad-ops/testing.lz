import math
def task(a, b, c, d, f):
     
     try:
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        f = float(f)
        print(f'Task: ({a} + {b}) / ({c} - {d}) + {f**0.5}')
        y = (a + b) / (c - d) + math.sqrt(f)
        print(f"Result: {y}")
        return y 
     except ZeroDivisionError:
        print("Divizion by zero")
        return "Divizion by zero"
     except ValueError:
        print("Datatype is invalid")
        return "Datatype is invalid"

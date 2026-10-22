print("The author of this program is Mariana Yatsenko.This program calculates the value of the expression by given x .Variant 99.")
import math

def f(x):
    """
    Calculate the value of the expression:
    sin(30/49) - 6π - 58e * 5/((x + 3)(x + 12)) - 13sin(x + 4) - sqrt(x + 15).
    """
    a = math.sin(30 / 49)
    b = 6 * math.pi
    c = 58 * math.exp(1) * (5 / ((x + 3) * (x + 12)))
    d = 13 * math.sin(x + 4)
    e = math.sqrt(x + 15)

    result = a - b - c - d - e
    return result

def main():
    try:
        x = float(input("For x: "))
        print(f"Entered x: {x}")

        if x >= -15 and x != -3 and x != -12:
            print("***** do calculations... done")
            result = f(x)
            print(f"result = {result}")
        else:
            print("result = undefined")
    except ZeroDivisionError:
        print("result = undefined")
    except ValueError:
        print("wrong input")

if __name__ == "__main__":
    main()


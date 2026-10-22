a=0.01
b=0.4

"""Обчислення значення виразу і функція нічого не перевіряє """
def s(x,eps):
    xsquared=x*x
    n=0
    a=1/x
    S=a
    while a>=eps or a<=-eps:
         tmp1=2*n-1
         tmp2=n+1
         a=a*((2*n+2)*tmp1*tmp1*xsquared/tmp2/tmp2/(2*n+1))
         n+=1
         S=S+a
    return S



try:
    print("I'm Mariana.Variant 99")
    x=float(input("Enter real x (0.01 <= x <= 0.4): "))
    if not (a <= x <= b):        
        raise Exception("out of domain")
    eps=float(input("Enter real epsilon (> 0): "))
    if eps <= 0:
        raise Exception("out of domain")

    print("*** do calculations ... ")
    result = s(x, eps)
    print("done")

    print(f"for x = {x:.7e}")
    print(f"for eps = {eps:.5e}")
    print(f"result = {result:.10f}")

    

except KeyboardInterrupt:
    print("\nprogram aborted")
    print("\n non-number value")

except ValueError:
    print("\nprogram aborted")
    print("\n non-number value")

except Exception:
    print("\n***** error")
    print("\nwrong value")


def is_float(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
print("Enter values in the form")
print("Ax+By=C")
print("Px+Qy=R")
while True:
    a1=input("A value of 1st equation:")
    b1=input("B value of 1st equation:")
    c1=input("C value of 1st equation:")

    a2=input("P value of 2nd equation:")
    b2=input("Q value of 2nd equation:")
    c2=input("R value of 2nd equation:")
    if is_float(a1) and is_float(b1) and is_float(c1) and is_float(a2) and is_float(b2) and is_float(c2):
        a1=float(a1)
        b1=float(b1)
        c1=float(c1)

        a2=float(a2)
        b2=float(b2)
        c2=float(c2)
        break
    else:
        print("If you entered all values correctly you should not get this\nAlso you have to enter all values again\n")
        continue
    
if a2/a1 == b2/b1:
    print("No solution")
else:
    print("There is solution")
    y=(((c2*a1/a2)-c1)/((b2*a1/a2)-b1))
    x=(c1-(b1*y))/a1
    y=round(y,3)
    x=round(x,3)
    print(f"X={x} and Y={y}")

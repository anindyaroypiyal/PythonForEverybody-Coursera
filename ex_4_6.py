def computepay(h,r):
    if h <= 40 and h >= 0:
        pay = hrs * rate
        return pay
    else:
        x = hrs - 40
        pay = 40 * rate + (x*rate*1.5)
        return pay


hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate:"))

p = computepay(hrs,rate)
print("Pay",p)

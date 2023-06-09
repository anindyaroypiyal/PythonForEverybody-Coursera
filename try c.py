hrs = float(input(Enter hours:))
rate = float(input(Enter rate:))
if hrs <= 40 and hrs >= 0:
    pay = hrs * rate
else:
    x = hrs - 40
    pay = 40 * rate + (x*rate*1.5)

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try :
        if num == "done" :
            break
        else:
            num = int(num)
    except :
        print('Invalid input')
        continue


    if largest is None :
        largest = num
        smallest = num
    elif num > largest:
        largest = num
    elif num < smallest:
        smallest = num


print("Maximum is", largest)
print("Minimum is", smallest)

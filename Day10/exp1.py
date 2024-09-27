try:
    width = float(input("please enter a triangle width: "))
    length = float(input("please enter a triangle length :"))
    if width == length:
        print("That's look like a square")
        exit()

    area = width * length
    print(area)
except ValueError:
    print("please enter a number")
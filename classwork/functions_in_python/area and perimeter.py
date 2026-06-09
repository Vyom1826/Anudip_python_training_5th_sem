from figures2D import *

while True:
    print("\n===== 2D FIGURE MENU =====")
    print("1. RECTANGLE")
    print("2. SQUARE")
    print("3. CIRCLE")
    print("4. Exit")

    figure = int(input("Enter your choice: "))

    if figure == 4:
        print("Exiting program...")
        break

    # Input dimensions based on selected figure
    if figure == 1:
        length = float(input("Enter length of the rectangle: "))
        breath = float(input("Enter braeth of the rectangle: "))

    elif figure == 2:
        side = float(input("Enter side of the square :"))

    elif figure == 3:
        radius = float(input("Enter radius of the circle :"))
    else:
        print("Invalid figure choice!")
        continue

    # Operation menu
    print("\n----- OPERATION MENU -----")
    print("1. Area")
    print("2. Perimeter")

    operation = int(input("Enter your choice: "))

    # Calculate result
    if figure == 1:  # RECTANGLE
        if operation == 1:
            result = area_rectangle(length,breath) 
            print("Area of Rectangle =", result)
        elif operation == 2:
            result = perimeter_rectangle(length,breath)
            print("Perimeter of Rectangle =", result)
        else:
            print("Invalid operation choice!")

    elif figure == 2:  # SQUARE
        if operation == 1:
            result = area_square(side)
            print("Area of Square =", result)
        elif operation == 2:
            result = perimeter_square(side)
            print("Perimeter of Square =", result)
        else:
            print("Invalid operation choice!")

    elif figure == 3:  # CIRCLE
        if operation == 1:
            result = area_circle(radius)
            print("Area of Circle =", result)
        elif operation == 2:
            result = perimeter_circle(radius)
            print("Perimeter of Circle =", result)
        else:
            print("Invalid operation choice!")


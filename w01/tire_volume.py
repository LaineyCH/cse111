"""
The size of a car tire in the United States is represented with three numbers like this: 205/60R15. 
The first number is the width of the tire in millimeters. The second number is the aspect ratio. 
The third number is the diameter in inches of the wheel that the tire fits. 
The volume of space inside a tire can be approximated with this formula:

v = (PI * (w**2) * a * ((w * a) + (2540 * d))) / 10000000000

v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.

"""

import math
from datetime import date

today = date.today()
price = 0
quantity = 0
total_cost = 0

# collect user inputs and save to variables
while True:
    print()
    width = int(input("Please enter the tire's width in mm (eg 205): "))
    aspect = int(input("Please enter the tire's aspect ratio (eg 60): "))
    diameter = int(input("Please enter the tire's diameter in inches (eg 15): "))

    #get price for width (165-385)
    if width == 165:
        if aspect == 65:
            if diameter == 14:
                price = 144.99
    elif width == 175:
        if aspect == 55:
            if diameter == 15:
                price = 244.99
        elif aspect == 65:
            if diameter == 14:
                price = 54.99
            elif diameter == 15:
                price = 92.99
        elif aspect == 70:
            if diameter == 13:
                price = 42.99
            elif diameter == 14:
                price = 51.99
    elif width == 185:
        if aspect == 55:
            if diameter == 15:
                price = 160.99
            elif diameter == 16:
                price = 124.99
        elif aspect == 60:
            if diameter == 14:
                price = 47.99
            elif diameter == 15:
                price = 94.99
            elif diameter == 16:
                price = 108.99
        elif aspect == 65:
            if diameter == 14:
                price = 50.99
            elif diameter == 15:
                price = 58.99
        elif aspect == 70:
            if diameter == 14:
                price = 51.99
    elif width == 195:
        if aspect == 50:
            if diameter == 15:
                price = 159.99
            elif diameter == 16:
                price = 125.99
        elif aspect == 55:
            if diameter == 15:
                price = 161.99
            elif diameter == 16:
                price = 129.99
        elif aspect == 60:
            if diameter == 15:
                price = 54.99
            elif diameter == 17:
                price = 189.99
        elif aspect == 65:
            if diameter == 15:
                price = 61.99
        elif aspect == 70:
            if diameter == 14:
                price = 56.99
        elif aspect == 75:
            if diameter == 14:
                price = 58.99
            elif diameter == 16:
                price = 162.99
    elif width == 205:
        if aspect == 35:
            if diameter == 18:
                price = 182.99
        elif aspect == 40:
            if diameter == 17:
                price = 124.99
        elif aspect == 45:
            if diameter == 16:
                price = 148.99
            elif diameter == 17:
                price = 133.99
        elif aspect == 50:
            if diameter == 15:
                price = 158.99
            elif diameter == 16:
                price = 121.99
            elif diameter == 17:
                price = 122.99
        elif aspect == 55:
            if diameter == 16:
                price = 69.99
            elif diameter == 17:
                price = 159.99
        elif aspect == 60:
            if diameter == 15:
                price = 63.99
            elif diameter == 16:
                price = 69.99
            elif diameter == 18:
                price = 218.99
        elif aspect == 65:
            if diameter == 15:
                price = 59.99
            elif diameter == 16:
                price = 73.99
        elif aspect == 70:
            if diameter == 15:
                price = 66.99
            elif diameter == 16:
                price = 158.99
        elif aspect == 75:
            if diameter == 14:
                price = 79.99
            elif diameter == 15:
                price = 73.99
    elif width == 215:
        if aspect == 40:
            if diameter == 18:
                price = 124.99
        elif aspect == 45:
            if diameter == 16:
                price = 148.99
            elif diameter == 17:
                price = 133.99
            elif diameter == 18:
                price = 163.99
        elif aspect == 50:
            if diameter == 17:
                price = 68.99
            elif diameter == 18:
                price = 121.99
        elif aspect == 55:
            if diameter == 16:
                price = 69.99
            elif diameter == 17:
                price = 143.99
            elif diameter == 18:
                price = 159.99
        elif aspect == 60:
            if diameter == 15:
                price = 63.99
            elif diameter == 16:
                price = 69.99
            elif diameter == 17:
                price = 89.99
        elif aspect == 65:
            if diameter == 15:
                price = 75.99
            elif diameter == 16:
                price = 89.99
            elif diameter == 17:
                price = 103.99
        elif aspect == 70:
            if diameter == 14:
                price = 66.99
            elif diameter == 15:
                price = 158.99
            elif diameter == 16:
                price = 188.99
            elif diameter == 17:
                price = 240.99
        elif aspect == 75:
            if diameter == 15:
                price = 66.99
        elif aspect == 85:
            if diameter == 16:
                price = 112.99
    elif width == 225:
        if aspect == 30:
            if diameter == 20:
                price = 189.99
        elif aspect == 35:
            if diameter == 18:
                price = 328.99
            elif diameter == 19:
                price = 425.99
            elif diameter == 20:
                price = 535.99
        elif aspect == 40:
            if diameter == 18:
                price = 81.99
            if diameter == 19:
                price = 198.99
        elif aspect == 45:
            if diameter == 15:
                price = 58.99
            elif diameter == 16:
                price = 83.99
            elif diameter == 17:
                price = 112.99
            elif diameter == 18:
                price = 133.99
            elif diameter == 19:
                price = 198.99
        elif aspect == 50:
            if diameter == 15:
                price = 213.99
            elif diameter == 16:
                price = 121.99
            elif diameter == 17:
                price = 68.99
            elif diameter == 18:
                price = 121.99
        elif aspect == 55:
            if diameter == 16:
                price = 69.99
            elif diameter == 17:
                price = 143.99
            elif diameter == 18:
                price = 159.99
            elif diameter == 19:
                price = 210.99
        elif aspect == 60:
            if diameter == 16:
                price = 63.99
            elif diameter == 17:
                price = 69.99
            elif diameter == 18:
                price = 89.99
        elif aspect == 65:
            if diameter == 16:
                price = 89.99
            elif diameter == 17:
                price = 103.99
        elif aspect == 70:
            if diameter == 15:
                price = 158.99
            elif diameter == 16:
                price = 188.99
        elif aspect == 75:
            if diameter == 15:
                price = 103.99
            elif diameter == 16:
                price = 159.99
            elif diameter == 17:
                price = 224.99
    elif width == 235:
        if aspect == 35:
            if diameter == 18:
                price = 182.99
            elif diameter == 20:
                price = 182.99
        elif aspect == 40:
            if diameter == 19:
                price = 124.99
            elif diameter == 20:
                price = 182.99
        elif aspect == 45:
            if diameter == 17:
                price = 148.99
            elif diameter == 18:
                price = 133.99
            elif diameter == 19:
                price = 224.99
            elif diameter == 20:
                price = 282.99
        elif aspect == 50:
            if diameter == 17:
                price = 69.99
            elif diameter == 18:
                price = 159.99
            elif diameter == 19:
                price = 169.99
            elif diameter == 20:
                price = 218.99
            elif diameter == 21:
                price = 369.99
        elif aspect == 55:
            if diameter == 17:
                price = 69.99
            elif diameter == 18:
                price = 159.99
            elif diameter == 19:
                price = 169.99
            elif diameter == 20:
                price = 218.99
        elif aspect == 60:
            if diameter == 16:
                price = 69.99
            elif diameter == 17:
                price = 109.99
            elif diameter == 18:
                price = 159.99
            elif diameter == 19:
                price = 169.99
            elif diameter == 20:
                price = 218.99
        elif aspect == 65:
            if diameter == 16:
                price = 59.99
            elif diameter == 17:
                price = 73.99
            elif diameter == 18:
                price = 173.99
        elif aspect == 70:
            if diameter == 15:
                price = 66.99
            elif diameter == 16:
                price = 158.99
            elif diameter == 17:
                price = 273.99
        elif aspect == 75:
            if diameter == 15:
                price = 66.99
            elif diameter == 16:
                price = 158.99
            elif diameter == 17:
                price = 273.99
        elif aspect == 80:
            if diameter == 17:
                price = 235.99
        elif aspect == 85:
            if diameter == 16:
                price = 108.99
    elif width == 245:
        if aspect == 35:
            if diameter == 18:
                price = 182.99
            elif diameter == 20:
                price = 182.99
        elif aspect == 40:
            if diameter == 19:
                price = 124.99
            elif diameter == 20:
                price = 182.99
        elif aspect == 45:
            if diameter == 17:
                price = 148.99
            elif diameter == 18:
                price = 133.99
            elif diameter == 19:
                price = 224.99
            elif diameter == 20:
                price = 282.99
        elif aspect == 50:
            if diameter == 17:
                price = 69.99
            elif diameter == 18:
                price = 159.99
            elif diameter == 19:
                price = 169.99
            elif diameter == 20:
                price = 218.99
            elif diameter == 21:
                price = 369.99
        elif aspect == 55:
            if diameter == 17:
                price = 69.99
            elif diameter == 18:
                price = 159.99
            elif diameter == 19:
                price = 169.99
            elif diameter == 20:
                price = 218.99
        elif aspect == 60:
            if diameter == 16:
                price = 69.99
            elif diameter == 17:
                price = 109.99
            elif diameter == 18:
                price = 159.99
            elif diameter == 19:
                price = 169.99
            elif diameter == 20:
                price = 218.99
        elif aspect == 65:
            if diameter == 16:
                price = 59.99
            elif diameter == 17:
                price = 73.99
            elif diameter == 18:
                price = 173.99
        elif aspect == 70:
            if diameter == 15:
                price = 66.99
            elif diameter == 16:
                price = 158.99
            elif diameter == 17:
                price = 273.99
        elif aspect == 75:
            if diameter == 15:
                price = 66.99
            elif diameter == 16:
                price = 158.99
            elif diameter == 17:
                price = 273.99
        elif aspect == 80:
            if diameter == 17:
                price = 235.99
        elif aspect == 85:
            if diameter == 16:
                price = 108.99
    elif width == 255:
        if aspect == 35:
            if diameter == 18:
                price = 182.99
            elif diameter == 20:
                price = 182.99
        elif aspect == 40:
            if diameter == 19:
                price = 124.99
            elif diameter == 20:
                price = 182.99
        elif aspect == 45:
            if diameter == 17:
                price = 148.99
            elif diameter == 18:
                price = 133.99
            elif diameter == 19:
                price = 224.99
            elif diameter == 20:
                price = 282.99
        elif aspect == 50:
            if diameter == 17:
                price = 69.99
            elif diameter == 18:
                price = 159.99
            elif diameter == 19:
                price = 169.99
            elif diameter == 20:
                price = 218.99
            elif diameter == 21:
                price = 369.99
        elif aspect == 55:
            if diameter == 17:
                price = 69.99
            elif diameter == 18:
                price = 159.99
            elif diameter == 19:
                price = 169.99
            elif diameter == 20:
                price = 218.99
        elif aspect == 60:
            if diameter == 16:
                price = 69.99
            elif diameter == 17:
                price = 109.99
            elif diameter == 18:
                price = 159.99
            elif diameter == 19:
                price = 169.99
            elif diameter == 20:
                price = 218.99
        elif aspect == 65:
            if diameter == 16:
                price = 59.99
            elif diameter == 17:
                price = 73.99
            elif diameter == 18:
                price = 173.99
        elif aspect == 70:
            if diameter == 15:
                price = 66.99
            elif diameter == 16:
                price = 158.99
            elif diameter == 17:
                price = 273.99
        elif aspect == 75:
            if diameter == 15:
                price = 66.99
            elif diameter == 16:
                price = 158.99
            elif diameter == 17:
                price = 273.99
        elif aspect == 80:
            if diameter == 17:
                price = 235.99
        elif aspect == 85:
            if diameter == 16:
                price = 108.99
    elif width == 265:
        if aspect == 30:
            if diameter == 18:
                price = 182.99
            elif diameter == 20:
                price = 182.99
        elif aspect == 35:
            if diameter == 18:
                price = 182.99
            elif diameter == 20:
                price = 182.99
        elif aspect == 40:
            if diameter == 19:
                price = 124.99
            elif diameter == 20:
                price = 182.99
        elif aspect == 45:
            if diameter == 17:
                price = 148.99
            elif diameter == 18:
                price = 133.99
            elif diameter == 19:
                price = 224.99
            elif diameter == 20:
                price = 282.99
        elif aspect == 50:
            if diameter == 17:
                price = 69.99
            elif diameter == 18:
                price = 159.99
            elif diameter == 19:
                price = 169.99
            elif diameter == 20:
                price = 218.99
            elif diameter == 21:
                price = 369.99
        elif aspect == 55:
            if diameter == 17:
                price = 69.99
            elif diameter == 18:
                price = 159.99
            elif diameter == 19:
                price = 169.99
            elif diameter == 20:
                price = 218.99
        elif aspect == 60:
            if diameter == 16:
                price = 69.99
            elif diameter == 17:
                price = 109.99
            elif diameter == 18:
                price = 159.99
            elif diameter == 19:
                price = 169.99
            elif diameter == 20:
                price = 218.99
        elif aspect == 65:
            if diameter == 16:
                price = 59.99
            elif diameter == 17:
                price = 73.99
            elif diameter == 18:
                price = 173.99
        elif aspect == 70:
            if diameter == 15:
                price = 66.99
            elif diameter == 16:
                price = 158.99
            elif diameter == 17:
                price = 273.99
        elif aspect == 75:
            if diameter == 15:
                price = 66.99
            elif diameter == 16:
                price = 158.99
            elif diameter == 17:
                price = 273.99
    elif width == 275:
        if aspect == 30:
            if diameter == 18:
                price = 182.99
            elif diameter == 20:
                price = 182.99
        elif aspect == 35:
            if diameter == 18:
                price = 182.99
            elif diameter == 20:
                price = 182.99
        elif aspect == 40:
            if diameter == 19:
                price = 124.99
            elif diameter == 20:
                price = 182.99
        elif aspect == 45:
            if diameter == 17:
                price = 148.99
            elif diameter == 18:
                price = 133.99
            elif diameter == 19:
                price = 224.99
            elif diameter == 20:
                price = 282.99
        elif aspect == 50:
            if diameter == 17:
                price = 69.99
            elif diameter == 18:
                price = 159.99
            elif diameter == 19:
                price = 169.99
            elif diameter == 20:
                price = 218.99
            elif diameter == 21:
                price = 369.99
        elif aspect == 55:
            if diameter == 17:
                price = 69.99
            elif diameter == 18:
                price = 159.99
            elif diameter == 19:
                price = 169.99
            elif diameter == 20:
                price = 218.99
        elif aspect == 60:
            if diameter == 16:
                price = 69.99
            elif diameter == 17:
                price = 109.99
            elif diameter == 18:
                price = 159.99
            elif diameter == 19:
                price = 169.99
            elif diameter == 20:
                price = 218.99
        elif aspect == 65:
            if diameter == 16:
                price = 59.99
            elif diameter == 17:
                price = 73.99
            elif diameter == 18:
                price = 173.99
        elif aspect == 70:
            if diameter == 15:
                price = 66.99
            elif diameter == 16:
                price = 158.99
            elif diameter == 17:
                price = 273.99
    else:
        price = 0

    if price == 0:
        print(f"I am sorry, we do not have that tire in stock, or the measurements you have specified are not valid.")
        try_again = input("Would you like to try agian? y/n: ")
        if try_again == "y" or try_again == "Y" or try_again == "yes" or try_again == "Yes" or try_again == "YES":
            print()
        else:
            print(f"Have a great day")
            break
    else:
        break

if price > 0:
    # calculate volume according to goven formula for volume
    volume = (math.pi * (width**2) * aspect * ((width * aspect) + (2540 * diameter))) / 10000000000

    # create string of 1.current date 2.width of the tire 3.aspect ratio of the tire
    # 4.diameter of the wheel 5.volume of the tire 6.price per tire
    info_string = f"{today}, {width}, {aspect}, {diameter}, {volume: .2f}, ${price: .2f}"

    # display volume and price
    print()
    print(f"The volume of the tire is {volume: .2f} liters")
    print(f"These tires cost ${price: .2f} each.")
    print()

    # ask is customer would like to purchase
    # if yes, ask for quantity, calculate and display total, collect customer phone number, save info to string.
    # if no, send message and end. Add "no sale" to string.
    answer = input("Wold you like to purchase tires? y/n: ")
    if answer == "y" or answer == "Y" or answer == "yes" or answer == "Yes" or answer == "YES":
        quantity = int(input("How many tires would you like to purchase? "))
        total_cost = price * quantity
        phone = input("Please enter your phone number: ")
        print(f"Your total is: ${total_cost: .2f}")
        print(f"Thank you for our custom, we will notify you when your tires are ready for collection.")
        info_string += f", {quantity}, ${total_cost: .2f}, {phone}"
    else:
        print(f"Thank you for contacting us, have a great day.")
        info_string += f" no sale"

    # appened info_string to volumes.txt
    with open("volumes.txt", 'a') as volumes_file:
        volumes_file.write(info_string + "\n")

print()
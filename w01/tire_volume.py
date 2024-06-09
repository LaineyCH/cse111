"""
The size of a car tire in the United States is represented with three numbers like this: 205/60R15. 
The first number is the width of the tire in millimeters. The second number is the aspect ratio. 
The third number is the diameter in inches of the wheel that the tire fits. 
The volume of space inside a tire can be approximated with this formula:

v = (π * (w**2) * a * ((w * a) + (2540 * d))) / 10000000000

v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
"""

import math
from datetime import date

# get today's date
today = date.today()
price = 0
quantity = 0
total_cost = 0

# ranges of valid tire sizes to test validity of customer input
valid_widths = {i for i in range(165, 385, 10)}
valid_aspects = {i for i in range(25, 85, 5)}
valid_diameters = {i for i in range(13, 22, 1)}

# dictionary of tire prices
pricing_logic = {
    165: {
        65: {
                14: 144.99,
        },
    },
    175: {
        55: {
                15: 244.99,
            },
        65: {
                14: 54.99,
                15: 92.99,
            },
        70: {
                13: 42.99,
                14: 51.99,
        },
    },
    185: {
        55: {
                15: 160.99,
                16: 124.99,
            },
        60: {
                14: 47.99,
                15: 94.99,
                16: 108.99,
            },
        65: {
                14: 50.99,
                15: 58.99,
            },
        70: {
                14: 51.99,
        },
    },
    195: {
        50: {
                15: 159.99,
                16: 125.99,
            },
        55: {
                15: 161.99,
                16: 129.99,
            },
        60: {
                15: 54.99,
                17: 189.99,
            },
        65: {
                15: 61.99,
            },
        70: {
                14: 56.99,
            },
        75: {
                14: 58.99,
                16: 162.99,
        },
    },
    205: {
        35: {
                18: 182.99,
            },
        40: {
                17: 124.99,
            },
        45: {
                16: 148.99,
                17: 133.99,
            },
        50: {
                15: 158.99,
                16: 121.99,
                17: 122.99,
            },
        55: {
                16: 69.99,
                17: 159.99,
            },
        60: {
                15: 63.99,
                16: 69.99,
                18: 218.99,
            },
        65: {
                15: 59.99,
                16: 73.99,
            },
        70: {
                15: 66.99,
                16: 158.99,
            },
        75: {
                14: 79.99,
                15: 73.99,
        },
    },
    215: {
        40: {
                18: 124.99,
            },
        45: {
                16: 148.99,
                17: 133.99,
                18: 163.99,
            },
        50: {
                17: 68.99,
                18: 121.99,
            },
        55: {
                16: 69.99,
                17: 143.99,
                18: 159.99,
            },
        60: {
                15: 63.99,
                16: 69.99,
                17: 89.99,
            },
        65: {
                15: 75.99,
                16: 89.99,
                17: 103.99,
            },
        70: {
                14: 66.99,
                15: 158.99,
                16: 188.99,
                17: 240.99,
            },
        75: {
                15: 66.99,
            },
        85: {
                16: 112.99,
        },
    },
    225: {
        30: {
                20: 189.99,
            },
        35: {
                18: 328.99,
                19: 425.99,
                20: 535.99,
            },
        40: {
                18: 81.99,
                19: 198.99,
            },
        45: {
                15: 58.99,
                16: 83.99,
                17: 112.99,
                18: 133.99,
                19: 198.99,
            },
        50: {
                15: 213.99,
                16: 121.99,
                17: 68.99,
                18: 121.99,
            },
        55: {
                16: 69.99,
                17: 143.99,
                18: 159.99,
                19: 210.99,
            },
        60: {
                16: 63.99,
                17: 69.99,
                18: 89.99,
            },
        65: {
                16: 89.99,
                17: 103.99,
            },
        70: {
                15: 158.99,
                16: 188.99,
            },
        75: {
                15: 103.99,
                16: 159.99,
                17: 224.99,
        },
    },
    235: {
        35: {
                18: 182.99,
                20: 182.99,
            },
        40: {
                19: 124.99,
                20: 182.99,
            },
        45: {
                17: 148.99,
                18: 133.99,
                19: 224.99,
                20: 282.99,
            },
        50: {
                17: 69.99,
                18: 159.99,
                19: 169.99,
                20: 218.99,
                21: 369.99,
            },
        55: {
                17: 69.99,
                18: 159.99,
                19: 169.99,
                20: 218.99,
            },
        60: {
                16: 69.99,
                17: 109.99,
                18: 159.99,
                19: 169.99,
                20: 218.99,
            },
        65: {
                16: 59.99,
                17: 73.99,
                18: 173.99,
            },
        70: {
                15: 66.99,
                16: 158.99,
                17: 273.99,
            },
        75: {
                15: 66.99,
                16: 158.99,
                17: 273.99,
            },
        80: {
                17: 235.99,
            },
        85: {
                16: 108.99,
        },
    },
    245: {
        35: {
                18: 182.99,
                20: 182.99,
            },
        40: {
                19: 124.99,
                20: 182.99,
            },
        45: {
                17: 148.99,
                18: 133.99,
                19: 224.99,
                20: 282.99,
            },
        50: {
                17: 69.99,
                18: 159.99,
                19: 169.99,
                20: 218.99,
                21: 369.99,
            },
        55: {
                17: 69.99,
                18: 159.99,
                19: 169.99,
                20: 218.99,
            },
        60: {
                16: 69.99,
                17: 109.99,
                18: 159.99,
                19: 169.99,
                20: 218.99,
            },
        65: {
                16: 59.99,
                17: 73.99,
                18: 173.99,
            },
        70: {
                15: 66.99,
                16: 158.99,
                17: 273.99,
            },
        75: {
                15: 66.99,
                16: 158.99,
                17: 273.99,
            },
        80: {
                17: 235.99,
            },
        85: {
                16: 108.99,
        },
    },
    255: {
        35: {
                18: 182.99,
                20: 182.99,
            },
        40: {
                19: 124.99,
                20: 182.99,
            },
        45: {
                17: 148.99,
                18: 133.99,
                19: 224.99,
                20: 282.99,
            },
        50: {
                17: 69.99,
                18: 159.99,
                19: 169.99,
                20: 218.99,
                21: 369.99,
            },
        55: {
                17: 69.99,
                18: 159.99,
                19: 169.99,
                20: 218.99,
            },
        60: {
                16: 69.99,
                17: 109.99,
                18: 159.99,
                19: 169.99,
                20: 218.99,
            },
        65: {
                16: 59.99,
                17: 73.99,
                18: 173.99,
            },
        70: {
                15: 66.99,
                16: 158.99,
                17: 273.99,
            },
        75: {
                15: 66.99,
                16: 158.99,
                17: 273.99,
            },
        80: {
                17: 235.99,
            },
        85: {
                16: 108.99,
        },
    },
    265: {
        30: {
                18: 182.99,
                20: 182.99,
            },
        35: {
                18: 182.99,
                20: 182.99,
            },
        40: {
                19: 124.99,
                20: 182.99,
            },
        45: {
                17: 148.99,
                18: 133.99,
                19: 224.99,
                20: 282.99,
            },
        50: {
                17: 69.99,
                18: 159.99,
                19: 169.99,
                20: 218.99,
                21: 369.99,
            },
        55: {
                17: 69.99,
                18: 159.99,
                19: 169.99,
                20: 218.99,
            },
        60: {
                16: 69.99,
                17: 109.99,
                18: 159.99,
                19: 169.99,
                20: 218.99,
            },
        65: {
                16: 59.99,
                17: 73.99,
                18: 173.99,
            },
        70: {
                15: 66.99,
                16: 158.99,
                17: 273.99,
            },
        75: {
                15: 66.99,
                16: 158.99,
                17: 273.99,
        },
    },
    275: {
        30: {
                18: 182.99,
                20: 182.99,
            },
        35: {
                18: 182.99,
                20: 182.99,
            },
        40: {
                19: 124.99,
                20: 182.99,
            },
        45: {
                17: 148.99,
                18: 133.99,
                19: 224.99,
                20: 282.99,
            },
        50: {
                17: 69.99,
                18: 159.99,
                19: 169.99,
                20: 218.99,
                21: 369.99,
            },
        55: {
                17: 69.99,
                18: 159.99,
                19: 169.99,
                20: 218.99,
            },
        60: {
                16: 69.99,
                17: 109.99,
                18: 159.99,
                19: 169.99,
                20: 218.99,
            },
        65: {
                16: 59.99,
                17: 73.99,
                18: 173.99,
            },
        70: {
                15: 66.99,
                16: 158.99,
                17: 273.99,
        },
    },
}

# collect user inputs and save to variables. Check for validity, prompt again if not valid.
while True:
    print()
    width = int(input("Please enter the tire's width in mm (eg 205): "))
    if width not in valid_widths:
        print(f"Invalid input, please try again.")
        continue
    aspect = int(input("Please enter the tire's aspect ratio (eg 60): "))
    if aspect not in valid_aspects:
        print(f"Invalid input, please try again.")
        continue
    diameter = int(input("Please enter the tire's diameter in inches (eg 15): "))
    if diameter not in valid_diameters:
        print(f"Invalid input, please try again.")
        continue

    # get price from dictionary
    price = pricing_logic.get(width, {}).get(aspect, {}).get(diameter, 0)

    # if price = 0, the tire is not in stock. Let customer try a different size or end with message
    if price == 0:
        print(f"I am sorry, we do not have that tire in stock.")
        try_again = input("Would you like to check a different size? y/n: ")
        if try_again == "y" or try_again == "Y" or try_again == "yes" or try_again == "Yes" or try_again == "YES":
            print()
        else:
            print(f"Have a great day")
            break
    else:
        break

# if the tire is in stock:
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
    # if yes, ask for quantity, calculate and display total, collect customer phone number, save additional info to string.
    # if no, send message and end. Add "no sale" to string.
    answer = input("Wold you like to place an order? y/n: ")
    if answer == "y" or answer == "Y" or answer == "yes" or answer == "Yes" or answer == "YES":
        quantity = int(input("Please enter the quanity of tires to order: "))
        total_cost = price * quantity
        phone = input("Please enter your phone number: ")
        print(f"Your total is: ${total_cost: .2f}")
        print(f"Thank you for your custom, we will notify you when your tire/s are ready for collection.")
        info_string += f", {quantity}, ${total_cost: .2f}, {phone}"
    else:
        print(f"Thank you for contacting us, have a great day.")
        info_string += f", no sale"

    # appened info_string to volumes.txt
    with open("volumes.txt", 'a') as volumes_file:
        volumes_file.write(info_string + "\n")

print()
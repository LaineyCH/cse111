import csv
from datetime import datetime
import random


def main():
    # Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.
    try:
        # call read distionary and save dictionary to be passed into the next function calls
        products_dict = read_dictionary("w05/products.csv", 0)
        # call print receipt
        print_receipt("w05/request.csv", products_dict)
    # handle exceptions
    except FileNotFoundError as not_found_err:
        print(not_found_err)
    except PermissionError as perm_err:
        print(perm_err)
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)

    
def print_coupon(customer_product_list):
    """
    Read contents of requested products csv file, select a random product, find its name in the products dictionary,
    and print a coupon for it.
    Parameters
      file_name: the file name of the customers's request
      products_dict: the product dictionary
    Return: None
    """
    DISCOUNT = 0.15
    # select product at random from product list
    random_product = random.choice(customer_product_list)
    # print the coupon
    print("      ***   COUPON   ***")
    print(f"Use this coupon to get {DISCOUNT*100:.0f}% off")
    print("   the following product:")
    print(f"   ***   {random_product}   ***")
    print()


def print_receipt(file_name, products_dict):
    """
    Read contents of requested products csv file, find each products price in the products dictionary,
    and print the customer's order.
    Parameters
      file_name: the file name of the customers's request
      products_dict: the product dictionary
    Return: customer_product_list - the list of product names requested by the customer
    """
    SALES_TAX = 0.06
    DISCOUNT = 0.10
    number_items = 0
    subtotal = 0
    tax = 0
    total = 0
    # customer product list will become a list of th enames of the products th ecustomer requested
    customer_product_list = []
    # Call the now() method to get the current date and time as a datetime object from the computer's operating system.
    current_date_and_time = datetime.now()
    
    print()
    print("ESL GROCERIES")
    print()

    #open csv file for reading
    with open(file_name, "rt") as csv_file:
        # Use the csv module to create a reader object that will read from the opened CSV file.
        reader = csv.reader(csv_file)
        # The first row of the CSV file contains column headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)
        # Read the rows in the CSV file one row at a time. The reader object returns each row as a list.
        for row_list in reader:
            # If the current row is not blank, add the data from the current to the dictionary.
            if len(row_list) != 0:
                # From the current row, retrieve the product key and the quantity, add quantity to items quantity
                product_key = row_list[0]
                quantity = int(row_list[1])
                number_items += quantity
                # using the product key, get the product list from the products didtionary
                product_list = products_dict[product_key]
                # from the product list retrieve the product name and price, calculate item price by quantity and add to subtotal
                name = product_list[1]
                price = float(product_list[2])
                item_total = price * quantity
                subtotal += item_total
                #print the product name, requested quantity and price (each)
                print(f"{name}: {quantity}@ ${price}")
                # add name to customer product list
                customer_product_list.append(name)
    # print receipt amounts
    print()
    print(f"Number of items: {number_items}")
    print(f"Subtotal: ${subtotal:.2f}")
    # add 10% discount if it is Tuesday or Wednesday
    if current_date_and_time.strftime("%A") in ["Tuesday", "Wednesday"]:
        disc = subtotal * DISCOUNT
        print(f"It's {current_date_and_time:%A}, you've received a {DISCOUNT*100:.0f}% discount!")
        print(f"Discount: ${disc:.2f}")
        subtotal -= disc
    tax = subtotal * SALES_TAX
    total = subtotal + tax
    print(f"Sales Tax (6%): ${tax:.2f}")
    print(f"TOTAL: ${total:.2f}")
    print()
    print(f"Thank you for shopping at ESL Groceries")
    # Use an f-string to print the current day of the week and the current time.
    print(f"{current_date_and_time:%A %d %b %Y %I:%M%p}")
    print()
    # call print coupon fuction to generate coupon based on the list of customer requested products
    print_coupon(customer_product_list)

    
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column to use as the keys in the dictionary.
    Return: a compound dictionary that contains the contents of the CSV file.
    """
    # Create an empty dictionary named csv_dict.
    csv_dict = {}
  
    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:
        # Use the csv module to create a reader object that will read from the opened CSV file.
        reader = csv.reader(csv_file)
        # The first row of the CSV file contains column headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)
        # Read the rows in the CSV file one row at a time. The reader object returns each row as a list.
        for row_list in reader:
            # If the current row is not blank, add the data from the current to the dictionary.
            if len(row_list) != 0:
                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]
                # Store the data from the current
                # row into the dictionary.
                csv_dict[key] = row_list
    # Return the dictionary.
    return csv_dict


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()

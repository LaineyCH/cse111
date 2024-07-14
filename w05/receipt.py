
import csv
from datetime import datetime
 
def main():
    try:
        # Read the products.csv file into a dictionary
        products_dict = read_dictionary('w05/products.csv', 0)
        print("MAURYS")

        print(products_dict)  # Print the dictionary
 

       
        total_items = 0
        subtotal = 0.0
 
        # Open the request.csv file and process it
        with open('w05/request.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                product_number = row[0]
                quantity= (row[1])
               
                # Get the product details from the products_dict
                product_info = products_dict.get(product_number, quantity)
                product_name = product_info[1]
                product_price = float(product_info[2])
                print(product_name, product_price)
                total_items += quantity
                Subtotal_cost = product_price * total_items
                # Calculate sales tax and total cost
                sales_tax = subtotal * 0.06
                total_cost = subtotal + sales_tax

        print("Requested Items")
        print(f"Total items ordered: {total_items}")
        print(f'The subtotal due: {Subtotal_cost} ')
        print(f'print the sales tax amount {sales_tax}')
        print(f'print the total amount due {total_cost}')
        print(f'Thank you')
        # Get the current date and time
        current_datetime = datetime.now()
        print("Current Date and Time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
                
    except KeyError:
        print(f"Error: Product number '{product_number}' not found in products data.")
    except FileNotFoundError:
        print("Error: The file 'request.csv' was not found.")
    except PermissionError:
        print("Error: Permission denied when trying to read the file 'request.csv'.")
    except Exception as e:
        print(f"An unexpected error occurred while processing the file 'request.csv': {e}")
        print("All Products")
 
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    return dictionary
 
 
 
# Call the main function
if __name__ == "__main__":
    main()
 
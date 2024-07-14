import csv


def main():
    student_dict = read_dictionary("w05/students.csv", 0)
    # loop to ask for user input - keeping looping until valid input is received
    while True:
        # ask user for input, strip white spaces
        i_number_input =  input("Please enter an I-Number: ").strip()
        # remove dashes
        i_number = i_number_input.replace("-", "")
        # check that all characters are numericall digits
        if not i_number.isdigit():
                print("Invalid I-Number")
        # check that the length is exactly 9
        elif len(i_number) != 9:
            if len(i_number) < 9:
                print("Invalid I-Number: too few digits" )
            elif len(i_number) > 9:
                print("Invalid I-Number: too many digits" )
        else:
            # if all is correct, leave while loop
            break
    # check if i-number is in student dictionary, if it is print student name, otherwise print "No such student"
    if i_number in student_dict:
        student_name = student_dict[i_number][1]
        print(student_name)
    else:
        print("No such student")


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
    student_dict = {}
    #open csv file for reading
    with open(filename, "rt") as csv_file:
        # Use the csv module to create a reader object that will read from the opened CSV file.
        reader = csv.reader(csv_file)
        # The first row of the CSV file contains column headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)
        # Read the rows in the CSV file one row at a time. The reader object returns each row as a list.
        for row_list in reader:
           key = row_list[key_column_index]
           student_dict[key] = row_list
    return student_dict


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
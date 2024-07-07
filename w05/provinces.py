# Modify the list read from a txt file
def main():
    print("")
    # Read the contents of a text file
    # named provinces.txt into a list.
    text_list = read_list("w05/provinces.txt")
    # Print the entire list.
    print(text_list)
    print("")

    # Remove the first element from the list.
    text_list.pop(0)
  
    # Remove the last element from the list.
    text_list.pop()

    print(text_list)
    print("")

    # Replace all occurrences of "AB" in the list with "Alberta".
    # Count the number of elements that are "Alberta" and print that number.
    alberta_count = 0
    for item in text_list:
        if item == "AB":
            index = text_list.index(item)
            text_list[index] = "Alberta"
            alberta_count += 1
        elif item == "Alberta":
            alberta_count += 1

    print(alberta_count)
    print("")
    
def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.
    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list that will store
    # the lines of text from the text file.
    text_list = []
    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:
        # Read the contents of the text
        # file one line at a time.
        for line in text_file:
            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()
            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)
    # Return the list that contains the lines of text.
    return text_list


# Call main to start this program.
if __name__ == "__main__":
    main()
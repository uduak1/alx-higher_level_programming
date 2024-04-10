#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    counter= 0  # Counter to track the number of elements printed
    try:
        for i in range(x):
            print(my_list[i], end=' ')  # Print the element without moving to a new line
            counter += 1  # Increment the counter for each element printed
    except IndexError:  # Handles the case when index is out of range
        pass  # Do nothing if the index is out of range
    finally:
        print()  # Move to a new line after printing all elements
        return counter  # Return the real number of elements printed


import sys
from one import say_hi


def any_function():
    # Read all input from standard input
    user_input = sys.stdin.read()

    # Print the input
    print("You entered:", user_input)


if __name__ == "__main__":
    any_function()
    # say_hi()

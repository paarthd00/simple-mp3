# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def validate_input(num):
    if type({num}) == 'int':
        print("")


def display_menu():
    # Prints menu
    menu_options = """
    1. Offline
    2. Online
    """

    print(f"" + menu_options)


def get_input():
    while 1:
        display_menu()
        val = input("choose option:")
        try:
            val = int(val)
            if isinstance(val, int):
                if val == 1:
                    print("Choose option  1")
                    break
                elif val == 2:
                    print("choose option 2")
                    break
        except ValueError:
            print("value error, Choose correct option")


if __name__ == '__main__':
    get_input()
    g = input("different prompt:")
    print(g)

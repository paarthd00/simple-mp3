# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




def get_input():
    val = input("choose option:")
    print("Choose option " + val)


def display_menu():
    # Prints menu
    menu_options = """
    1. Offline
    2. Online
    """
    print(f"" + menu_options)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    display_menu()
    get_input()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

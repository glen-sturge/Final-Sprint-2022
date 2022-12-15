# Main script for HAB Taxi Company.
# Author: Glen Sturge           Date: 2022-10-30

# Imports
import program_fun as pf
import globals

globals.init_defaults()

# Main Script
def main():
    while True:
        # Output program menu
        print()
        print("HAB Taxi Company")
        print("Company Services System")
        print()
        print("1.  Enter a New Employee (driver).")
        print("2.  Enter Company Revenues.")
        print("3.  Enter Company Expenses.")
        print("4.  Track Car Rentals.")
        print("5.  Record Employee Payment.")
        print("6.  Print Company Profit Listing.")
        print("7.  Print Driver Financial Listing.")
        print("8.  Your report – add description here.")
        print("9.  Quit Program.")
        print()

        # Get selection
        user_select = 0
        while True:
            try:
                user_select = int(input("    Enter choice (1-9): "))
            except ValueError:
                print("\n    That's Not A Digit!\n")
                continue
            if not (1 <= user_select <= 9):
                print("\n    That number is too big or too small!\n")
                continue
            else:
                break

        if user_select == 1:
            print()
            pf.choice_1()
            print()
        elif user_select == 2:
            print()
            pf.choice_2()
            print()
        elif user_select == 3:
            print()
            pf.choice_3()
            print()
        elif user_select == 4:
            print()
            pf.choice_4()
            print()
        elif user_select == 5:
            print()
            pf.choice_5()
            print()
        elif user_select == 6:
            print()
            pf.choice_6()
            print()
        elif user_select == 7:
            print()
            pf.choice_7()
            print()
        elif user_select == 8:
            print()
            pf.choice_8()
            print()
        else:
            globals.save_defaults()
            print()
            print("\nHave A Nice Day!")
            break


if __name__ == '__main__':
    main()

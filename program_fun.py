import fmt_fun as ff
import valid_fun as vf
import datetime
import globals

dt = datetime.datetime

# Constants
PROV_CODES = ["AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YT"]


def choice_1():
    print("Enter a New Employee (driver).\n")

    """
    List of data fields.
    
    DriverNum - PK
    EmpFN
    EmpLN
    StreetAddress
    City
    Prov
    PostalCode
    Phone
    DLNum
    DLExpiry
    InsurPolCom
    InsurPolNum
    OwnCarOption
    BalDue (StandFees, RentalFees(weekly/daily?)) initialize to zero for record. to be updated elsewhere.
    """

    while True:
        emp_fn = input(ff.f_inp_f40("Enter Employee First Name")).title()
        if vf.not_blank(emp_fn):
            break

    while True:
        emp_ln = input(ff.f_inp_f40("Enter Employee Last Name")).title()
        if vf.not_blank(emp_ln):
            break

    while True:
        emp_street = input(ff.f_inp_f40("Enter Employee Street Address"))
        if vf.not_blank(emp_street):
            emp_street = ff.f_space_cap(emp_street)
            break

    while True:
        emp_city = input(ff.f_inp_f40("Enter Employee City"))
        if vf.not_blank(emp_city):
            emp_city = ff.f_space_cap(emp_city)
            break

    while True:
        print(PROV_CODES)
        print()
        emp_prov = input(ff.f_inp_f40("Enter Employee Province Code")).upper()
        if emp_prov in PROV_CODES:
            break
        else:
            print("\nNot A Valid Province Code. Try Again.\n")

    while True:
        print("\nPostal Code Format : L#L#L#\n")
        emp_postal = input(ff.f_inp_f40("Enter Employee Postal Code")).upper()
        if vf.check_postal(emp_postal):
            break

    while True:
        print("\nPhone Format : ###-###-####\n")
        emp_phone = input(ff.f_inp_f40("Enter Employee 10-Digit Phone"))
        if vf.check_phone(emp_phone):
            break

    while True:
        emp_diver_lic_num = input(ff.f_inp_f40("Enter Employee Driver's License Number")).upper()
        if vf.not_blank(emp_diver_lic_num):
            break

    while True:
        print("\nExpiry Format: YYYY-MM-DD\n")
        emp_driver_lic_expiry = input(ff.f_inp_f40("Enter Employee Drivers License Expiry"))
        if vf.check_date_std(emp_driver_lic_expiry):
            break

    while True:
        emp_insure_comp = input(ff.f_inp_f40("Enter Employee's Insurance Company"))
        if vf.not_blank(emp_insure_comp):
            emp_insure_comp = ff.f_space_cap(emp_insure_comp)
            break

    while True:
        emp_insure_num = input(ff.f_inp_f40("Enter Employee's Insurance Number"))
        if vf.not_blank(emp_insure_num):
            break

    while True:
        emp_vehicle = input(ff.f_inp_f40("Employee Using Own Vehicle Or Rented? (O/R)")).upper()
        if emp_vehicle == 'O' or emp_vehicle == 'R':
            break

    emp_bal_due = 0

    # Add data to Rentals File
    with open("Employees.dat", "a") as f:
        f.write("{}, ".format(globals.NEXT_DRIVER_NUM))
        f.write("{}, ".format(emp_fn))
        f.write("{}, ".format(emp_ln))
        f.write("{}, ".format(emp_street))
        f.write("{}, ".format(emp_city))
        f.write("{}, ".format(emp_prov))
        f.write("{}, ".format(emp_postal))
        f.write("{}, ".format(emp_phone))
        f.write("{}, ".format(emp_diver_lic_num))
        f.write("{}, ".format(emp_driver_lic_expiry))
        f.write("{}, ".format(emp_insure_comp))
        f.write("{}, ".format(emp_insure_num))
        f.write("{}, ".format(emp_vehicle))
        f.write("{}\n".format(emp_bal_due))

    print("\nNew Employee Data Saved...")

    globals.NEXT_DRIVER_NUM += 1

    hold_screen = input("\nPress Enter To Continue...")


def choice_2():
    print("Enter Company Revenues.\n")
    hold_screen = input("Press Enter To Continue...")


def choice_3():
    print("Enter Company Expenses.\n")
    hold_screen = input("Press Enter To Continue...")


def choice_4():
    print("Track Car Rentals.\n")

    f = open("Employees.dat", "r")
    for data in f:
        Dataline = data.split(",")
        DriverNumList = Dataline[0].strip()

    # User Inputs
    DriverNum = input("Please enter your driver number: ")
    f = open("Employees.dat", "r")
    for data in f:
        Dataline = data.split(",")
        if Dataline[0].strip() == DriverNum:
            Name = f"{Dataline[1]}, {Dataline[2]}"
            break

    while True:
        RentalStartDate = input("Enter the rental start date: (YYYY-MM-DD) ")
        if RentalStartDate == "":
            print("The rental start date cannot be left blank.")
        elif len(RentalStartDate) != 10:
            print("Please enter the rental start date in the proper format.")
        else:
            break
    while True:
        try:
            CarNum = int(input("Enter the car number: "))
        except:
            print("Please enter a valid number.")
        else:
            if CarNum > 4 or CarNum < 1:
                print("The car number must be between 1 and 4.")
            else:
                break
    while True:
        try:
            RentalLength = int(input("Enter the rental length: (Day(1), Week(7) or enter a number of days) "))
        except:
            print("Please enter a valid number.")
        else:
            break

    # Calculations
    print()
    RentalCost = RentalLength * globals.DAILY_RENTAL_FEE
    print("Rental Cost:", ff.f_dol_com_2d(RentalCost))
    HST = RentalCost * globals.HST_RATE
    print("HST:", ff.f_dol_com_2d(HST))
    Total = RentalCost + HST
    print("Total:", ff.f_dol_com_2d(Total))
    print()

    # Add data to Rentals File
    f = open("Rentals.dat", "a")

    f.write("{}, ".format(globals.RENTAL_ID))
    f.write("{}, ".format(DriverNum))
    f.write("{}, ".format(RentalStartDate))
    f.write("{}, ".format(CarNum))
    f.write("{}, ".format(RentalLength))
    f.write("{}, ".format(RentalCost))
    f.write("{}, ".format(HST))
    f.write("{}\n".format(Total))

    f.close()

    print("Rental information saved.")

    globals.RENTAL_ID += 1
    hold_screen = input("Press Enter To Continue...")

def choice_5():
    print("Record Employee Payment.\n")
    # Imports
    import datetime

    # Variables
    End = "Y"
    today = datetime.datetime.now()

    f = open("Employees.dat", "r")
    for data in f:
        Dataline = data.split(",")
        DriverNumList = Dataline[0].strip()


    # Inputs
    while End == "Y":
        DriverNum = input("Please enter your driver number: ")
        f = open("Employees.dat", "r")
        for data in f:
            Dataline = data.split(",")
            if Dataline[0].strip() == DriverNum:
                Name = f"{Dataline[1]}, {Dataline[2]}"
                break


        PaymentAmount = input("Please enter the payment amount: ")
        PaymentReason = input("Please enter the payment reason: ")
        PaymentMethod = input("Please enter the payment method (D - debit, C - cash, V - visa): ").upper()

        # Receipt if card or visa is chosen
        if PaymentMethod == "D" or PaymentMethod == "V":

            CardNum = input("Please enter your card number: ")

            if len(CardNum) == 16:
                print("=============================================================================")
                print(f"Driver Number: {DriverNum}                    Payment Information ")
                print(f"Name: {Name}                           Payment Reason: {PaymentReason}")
                print(f"Date: {today.strftime('%Y-%m-%d')}                       Payment Method: {PaymentMethod}")
                print(f"                                       Payment Amount: {PaymentAmount}")
                print(f"                                       Card Number: {CardNum}")
                print("=============================================================================")
        else:
            CardNum = "Cash Payment Used"
            print("=============================================================================")
            print(f"Driver Number: {DriverNum}                    Payment Information ")
            print(f"Name: {Name}                           Payment Reason: {PaymentReason}")
            print(f"Date: {today.strftime('%Y-%m-%d')}                       Payment Method: {PaymentMethod}")
            print(f"                                       Payment Amount: {PaymentAmount}")
            print("=============================================================================")

        f = open("EmployeePaymentRecords.dat", "a")
        f.write("{}, ".format(globals.PAYMENT_ID))
        f.write("{}, ".format(DriverNum))
        f.write("{}, ".format(PaymentAmount))
        f.write("{}, ".format(PaymentReason))
        f.write("{}, ".format(PaymentMethod))
        f.write("{}, ".format(CardNum))
        f.write("{}\n ".format(today.strftime('%Y-%m-%d')))

        globals.PAYMENT_ID += 1

        # End of loop statement
        End = input(
            "Would you like the end the program or enter another payment record (Y - Enter another, N - End program): ").upper()

        if End == "N":
            print("Payment details recorded!")
        break
    hold_screen = input("Press Enter To Continue...")


def choice_6():
    print("Print Company Profit Listing.\n")
    hold_screen = input("Press Enter To Continue...")


def choice_7():
    print("Print Driver Financial Listing.\n")
    hold_screen = input("Press Enter To Continue...")


def choice_8():
    print("Your report – add description here. (To Be Updated)\n")
    hold_screen = input("Press Enter To Continue...")

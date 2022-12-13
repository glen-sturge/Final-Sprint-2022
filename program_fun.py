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
    hold_screen = input("Press Enter To Continue...")


def choice_5():
    print("Record Employee Payment.\n")
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

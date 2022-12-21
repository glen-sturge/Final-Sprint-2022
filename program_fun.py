import fmt_fun as ff
import valid_fun as vf
import datetime
import globals

dt = datetime.datetime

# Constants
PROV_CODES = ["AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YT"]


def choice_1():
    print("Enter a New Employee (driver).\n")

    # Inputs
    # |First Name
    while True:
        emp_fn = input(ff.f_inp_f40("Enter Employee First Name")).title()
        if vf.not_blank(emp_fn):
            break

    # |Last Name
    while True:
        emp_ln = input(ff.f_inp_f40("Enter Employee Last Name")).title()
        if vf.not_blank(emp_ln):
            break

    # |Street Address
    while True:
        emp_street = input(ff.f_inp_f40("Enter Employee Street Address"))
        if vf.not_blank(emp_street):
            emp_street = ff.f_space_cap(emp_street)
            break

    # |City
    while True:
        emp_city = input(ff.f_inp_f40("Enter Employee City"))
        if vf.not_blank(emp_city):
            emp_city = ff.f_space_cap(emp_city)
            break

    # |Province
    while True:
        print(PROV_CODES)
        print()
        emp_prov = input(ff.f_inp_f40("Enter Employee Province Code")).upper()
        if emp_prov in PROV_CODES:
            break
        else:
            print("\nNot A Valid Province Code. Try Again.\n")

    # |Postal Code
    while True:
        print("\nPostal Code Format : L#L#L#\n")
        emp_postal = input(ff.f_inp_f40("Enter Employee Postal Code")).upper()
        if vf.check_postal(emp_postal):
            break

    # |Phone
    while True:
        print("\nPhone Format : ###-###-####\n")
        emp_phone = input(ff.f_inp_f40("Enter Employee 10-Digit Phone"))
        if vf.check_phone(emp_phone):
            break

    # |Driver's License
    while True:
        emp_diver_lic_num = input(ff.f_inp_f40("Enter Employee Driver's License Number")).upper()
        if vf.not_blank(emp_diver_lic_num):
            break

    # |Driver's License Expiry Date
    while True:
        print("\nExpiry Format: YYYY-MM-DD\n")
        emp_driver_lic_expiry = input(ff.f_inp_f40("Enter Employee Drivers License Expiry"))
        if vf.check_date_std(emp_driver_lic_expiry):
            break

    # |Insurance Company
    while True:
        emp_insure_comp = input(ff.f_inp_f40("Enter Employee's Insurance Company"))
        if vf.not_blank(emp_insure_comp):
            emp_insure_comp = ff.f_space_cap(emp_insure_comp)
            break

    # |Insurance Number
    while True:
        emp_insure_num = input(ff.f_inp_f40("Enter Employee's Insurance Number"))
        if vf.not_blank(emp_insure_num):
            break

    # |Own Or Rented Vehicle
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
    # Option not selected
    print("Enter Company Revenues.\n")
    hold_screen = input("Press Enter To Continue...")


def choice_3():
    # Option not selected
    print("Enter Company Expenses.\n")
    hold_screen = input("Press Enter To Continue...")


def choice_4():
    print("Track Car Rentals.\n")

    # f = open("Employees.dat", "r")
    # for data in f:
    #     Dataline = data.split(",")
    #     DriverNumList = Dataline[0].strip()

    # User Inputs
    # DriverNum = input("Please enter your driver number: ")
    # f = open("Employees.dat", "r")
    # for data in f:
    #     Dataline = data.split(",")
    #     if Dataline[0].strip() == DriverNum:
    #         Name = f"{Dataline[1]}, {Dataline[2]}"
    #         break

    # Get Driver Number & verify it exists in Employees.dat
    while True:
        Name = ""
        DriverFound = False
        DriverNum = input("Please enter your driver number: ")
        f = open("Employees.dat", "r")
        for data in f:
            Dataline = data.split(",")
            if Dataline[0].strip() == DriverNum:
                Name = f"{Dataline[1].strip()} {Dataline[2].strip()}"
                DriverFound = True
                break
        if DriverFound:
            print(f"{Name} Found!")
            break
        else:
            print("Driver Number Doesn't Exist! Try Again.")

    while True:
        RentalStartDate = input("Enter the rental start date: (YYYY-MM-DD) ")
        if vf.check_date_std(RentalStartDate):
            break
        # if RentalStartDate == "":
        #     print("The rental start date cannot be left blank.")
        # elif len(RentalStartDate) != 10:
        #     print("Please enter the rental start date in the proper format.")
        # else:
        #     break

    while True:
        try:
            CarNum = int(input("Enter the car number: "))
        except ValueError:
            print("Please enter a valid number.")
        else:
            if CarNum > 4 or CarNum < 1:
                print("The car number must be between 1 and 4.")
            else:
                break

    while True:
        try:
            RentalLength = int(input("Enter the rental length: (Day(1), Week(7) or enter a number of days) "))
        except ValueError:
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

    # Variables
    Proceed = "Y"
    today = dt.now()

    # Inputs
    while Proceed == "Y":

        while True:
            Name = ""
            DriverFound = False
            DriverNum = input("Enter The Driver Number: ")
            f = open("Employees.dat", "r")
            for data in f:
                Dataline = data.split(",")
                if Dataline[0].strip() == DriverNum:
                    Name = f"{Dataline[1].strip()} {Dataline[2].strip()}"
                    DriverFound = True
                    break
            if DriverFound:
                print(f"{Name} Found!")
                break
            else:
                print("Driver Number Doesn't Exist! Try Again.")

        # Get Payment Amount
        while True:
            try:
                PaymentAmount = float(input("Enter The Payment Amount: "))
            except ValueError:
                print("Not A Number. Try Again.")
            else:
                break

        # Get Payment Reason
        while True:
            PaymentReason = input("Enter The Payment Reason: ")
            if vf.not_blank(PaymentReason):
                break

        # Get Payment Method
        while True:
            PaymentMethod = input("Paying With Debit, Cash, or Visa? (D/C/V) : ").upper()
            if PaymentMethod == 'D' or PaymentMethod == 'C' or PaymentMethod == 'V':
                break
            else:
                print("Error! Check Input And Try Again!")

        # Get card number or assign placeholder value for cash.
        while True:
            if PaymentMethod == "D" or PaymentMethod == "V":
                CardNum = input("Please enter your 16-digit card number: ")
                if len(CardNum) == 16 and CardNum.isdigit():
                    break
                else:
                    print("Invalid Entry. Try Again.")
            else:
                CardNum = "Paid Cash"
                break

        f = open("EmployeePaymentRecords.dat", "a")
        f.write("{}, ".format(globals.PAYMENT_ID))
        f.write("{}, ".format(DriverNum))
        f.write("{}, ".format(PaymentAmount))
        f.write("{}, ".format(PaymentReason))
        f.write("{}, ".format(PaymentMethod))
        f.write("{}, ".format(CardNum))
        f.write("{}\n".format(today.strftime('%Y-%m-%d')))

        print("\nEmployee Payment Record Saved...")

        globals.PAYMENT_ID += 1

        # End of loop statement
        while True:
            Proceed = input("\nProcess Another Payment? (Y/N) : ").upper()
            if Proceed == "Y" or Proceed == "N":
                break
            else:
                print("Error! Try Again.")

        if Proceed == "N":
            break

    hold_screen = input("\nPress Enter To Continue...")


def choice_6():
    print("Print Company Profit Listing.\n")
    hold_screen = input("Press Enter To Continue...")


def choice_7():
    print("Print Driver Financial Listing.\n")

    driverNumInput = input("Enter your driver number: ")
    startDateStr = input("Enter the start date of listings you would like to print: (YYYY-MM-DD) ")
    startDate = dt.strptime(startDateStr, "%Y-%m-%d")
    endDateStr = input("Enter the end date of listings you would like to print: (YYYY-MM-DD) ")
    endDate = dt.strptime(endDateStr, "%Y-%m-%d")

    print()
    print("HAB TAXI SERVICES")
    print("DRIVER FINANCIAL LISTING FROM", startDateStr, "to", endDateStr)
    print()
    print("DRIVER   TRANS    TRANS         TRANS")
    print("NUMBER   ID       DATE          DESCRIPTION   SUBTOTAL   HST     TOTAL")
    print("=======================================================================")

    f = open("Revenue.dat", "r")
    GrandSubtotal = 0
    TotalHST = 0
    GrandTotal = 0
    for data in f:
        Dataline = data.split(",")
        DriverNum = Dataline[3].strip()
        TransID = Dataline[0].strip()
        TransDateStr = Dataline[1].strip()
        TransDate = dt.strptime(TransDateStr, "%Y-%m-%d")
        TransDescrip = Dataline[2].strip()
        Subtotal = float(Dataline[4].strip())
        HST = float(Dataline[5].strip())
        Total = float(Dataline[6].strip())
        if TransDate >= startDate and TransDate <= endDate:
            if driverNumInput == DriverNum:
                print(DriverNum, "   ", TransID, "     ", TransDateStr, "   ", TransDescrip, "    ",
                      ff.f_dol_com_2d(Subtotal), "   ", ff.f_dol_com_2d(HST), " ", ff.f_dol_com_2d(Total))
                GrandSubtotal += float(Subtotal)
                TotalHST += float(HST)
                GrandTotal += float(Total)
    print("=======================================================================")
    print(f"TOTAL BEFORE TAXES: {ff.f_dol_com_2d(GrandSubtotal):>8s}")
    print(f"HST:                {ff.f_dol_com_2d(TotalHST):>8s}")
    print(f"TOTAL AFTER TAXES:  {ff.f_dol_com_2d(GrandTotal):>8s}")

    hold_screen = input("Press Enter To Continue...")


def choice_8():
    print("Your report – add description here. (To Be Updated)\n")

    #  FINAL SPRINT - HAB TAXI SERVICE - OPTION 8
    #  TO GENERATE A REPORT FOR RENTED CAR INVENTORY
    #  AUTHOR:  KIMBERLEY SNOW      DATE:  DEC 8, 2022

    import datetime
    import FormatValues as FV

    Today = datetime.datetime.now()

    #  REPORT FORMATTING - PRINTED LANDSCAPE

    #        1         2         3         4         5         6         7          8         9         10
    # 345678901234567890123456789012345678901234567890123456789012345678901213456789012345678901234567890
    print()
    print("HAB TAXI SERVICES")
    print(f"INVENTORY REPORT")
    print(f"{FV.FDateL(Today)}")
    print()
    print(f" CAR       RENTAL       YEAR/MAKE/MODEL             PLATE        PLATE       VIN")
    print(f" NUMBER    ID                                       NUMBER       EXPIRY      NUMBER")
    print("====================================================================================")
    RecordCtr = 0

    f = open("FleetInventory.dat", "r")
    for InventoryDataLine in f:
        InvLine = InventoryDataLine.split(",")
        CarNum = InvLine[0].strip()
        RentalID = InvLine[1].strip()
        Year = InvLine[2].strip()
        Make = InvLine[3].strip()
        Model = InvLine[4].strip()
        PlateNo = InvLine[5].strip()
        PlateExp = InvLine[6].strip()
        VinNum = InvLine[7].strip()
        print(
            f" {CarNum}        {RentalID:<6s}       {Year:<4s} {Make:<6s} {Model:<6s}"
            f"          {PlateNo:<6s}       {PlateExp:<7s}     {VinNum:<5s}")
        RecordCtr += 1
    f.close()
    print("====================================================================================")
    print(f"Total Vehicles in Fleet:  {RecordCtr}")

    hold_screen = input("Press Enter To Continue...")

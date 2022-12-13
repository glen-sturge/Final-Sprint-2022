# globals.py

def init_defaults():
    with open("Defaults.dat", "r") as d:
        global NEXT_TRANS_NUM
        NEXT_TRANS_NUM = int(d.readline().strip())
        global NEXT_DRIVER_NUM
        NEXT_DRIVER_NUM = int(d.readline().strip())
        global RENTAL_ID
        RENTAL_ID = int(d.readline().strip())
        global PAYMENT_ID
        PAYMENT_ID = int(d.readline().strip())
        global MONTHLY_STAND_FEE
        MONTHLY_STAND_FEE = float(d.readline().strip())
        global DAILY_RENTAL_FEE
        DAILY_RENTAL_FEE = float(d.readline().strip())
        global WEEKLY_RENTAL_FEE
        WEEKLY_RENTAL_FEE = float(d.readline().strip())
        global HST_RATE
        HST_RATE = float(d.readline().strip())


def save_defaults():
    with open("Defaults.dat", "w") as d:
        d.write("{}\n".format(str(NEXT_TRANS_NUM)))
        d.write("{}\n".format(str(NEXT_DRIVER_NUM)))
        d.write("{}\n".format(str(RENTAL_ID)))
        d.write("{}\n".format(str(PAYMENT_ID)))
        d.write("{}\n".format(str(MONTHLY_STAND_FEE)))
        d.write("{}\n".format(str(DAILY_RENTAL_FEE)))
        d.write("{}\n".format(str(WEEKLY_RENTAL_FEE)))
        d.write("{}\n".format(str(HST_RATE)))
        print("\nDefault Data Saved...")

def register():
    import datetime
    # =========full name ==========

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")

    # ======== date of birth ===========
    year = int(input("pls enter the year you were born: "))
    try:
        month = int(input("Enter the month you were born: "))
    except ValueError:
        print("Enter month of birth should be number\nexample 3 = march")
    day = int(input("Enter the day you were born: "))
    Dob = datetime.datetime(year, month, day)
    calc = (datetime.datetime.now() - Dob)
    convert_days = int(calc.days)
    Age = (convert_days / 365)
    if Age < 18:
        print("you are below 18years\nthis App is for 18+")
        exit()

    # ========== password ==========
    import time
    attempt = 5
    while True:
        pa = input("choose a password: ")
        confirm_password = input("confirm password: ")
        attempt -= 1
        if attempt == 0:
            print("Try registering again")
            exit()
        elif len(pa) < 6:
            print("password not strong\nIt must be more than 7")
        elif pa.isalpha():
            print("password must contain a number")
        elif pa != confirm_password:
            print("password didn't match with confirm ")
        else:
            print("Checking password...")
            time.sleep(5)

            print("Password accepted")
            break

    print("Loading...\nRegistration successful")


register()









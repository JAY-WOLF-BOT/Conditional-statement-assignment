
working_days = 200
absented_days = int(input("How many days have you been absent: "))
fees = 2000
paid_fee = int(input("How much have you paid for fees: "))


days_in_school = working_days - absented_days
days_percentage = (days_in_school/working_days) * 100



if days_percentage < 75:
    print("You are not eligible to write this exams!")
    if paid_fee != fees:
        print("School fees not paid fulling not eligible to write this exam")
else:
    print("You are eligible to write this exams!")    
# Python program to display calendar
from datetime import date

today = date.today()

print('')


def current_date():
    today = date.today()
    return today.strftime("%d/%m/%Y")


print(current_date())

import calendar

def fxn(year, month, day):
    variable = calendar.monthrange(year, month)

    return int(1<=day<=variable[1])


print(fxn(2022,2,29))
year = int(input("Enter a year: "))
# A leap year is defined as:
# one time in 4 years
# but not in 100 years
# but again in 400 years
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
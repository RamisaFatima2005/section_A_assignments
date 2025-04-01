# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):# There are 5 seconds in a year!

days_per_year = 365
hours_per_day = 24
min_per_hour = 60
sec_per_min = 60

def cal():
    seconds = days_per_year * hours_per_day * min_per_hour * sec_per_min
    print(f"There are {seconds} seconds in a year!")

cal()
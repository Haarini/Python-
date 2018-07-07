year=int(raw input())
print is_leap(year)
def is_leap(year):
    leap = False
    return bool(not year % 4 and (year % 100 or not year % 400))

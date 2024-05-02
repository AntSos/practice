# A simple program from PI course, it takes a year and a month and recognize if is leao year or common

def is_year_leap(year):
# Your code from LAB 4.3.1.6.

    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        return True
    else:
        return None
       
def days_in_month(year, month):

    months = {1:31, 2:[28, 29], 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    m = list (months.keys ())
    t_d = list (months.values ())
   
    if is_year_leap(year) is None and month == 2:
        d_r = t_d [month - 1][0]
   
    elif is_year_leap(year) is True and month == 2:
        d_r = t_d [month - 1][1]
       
    else:
        d_r = t_d [month - 1]
   
    return d_r

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

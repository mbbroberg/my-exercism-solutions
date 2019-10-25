def leap_year(x):
    return x%4==0 and (not x%100==0 or x%400==0)

print(leap_year(1600))
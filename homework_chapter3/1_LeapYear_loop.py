def find_leap_years(start, end):
    leap_years = []
    for year in range(start, end+1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years.append(year)
    return leap_years

start_year = 2000
end_year = 4000
leap_years = find_leap_years(start_year, end_year)

for i, year in enumerate(leap_years):
    print(year, end=' ')
    if (i + 1) % 10 == 0:
        print()

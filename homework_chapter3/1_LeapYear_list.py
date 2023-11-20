start_year = 2000
end_year = 4000

leap_years = [year for year in range(start_year, end_year+1) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]

for i, year in enumerate(leap_years):
    print(year, end=' ')
    if (i + 1) % 10 == 0:
        print()

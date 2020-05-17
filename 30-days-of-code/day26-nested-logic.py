from datetime import date


day, month, year = tuple(map(int, input().split()))
actual = date(day=day, month=month, year=year)

day, month, year = tuple(map(int, input().split()))
due = date(day=day, month=month, year=year)

fine = 0

if actual > due:
    if actual.year == due.year:
        if actual.month == due.month:
            fine = 15 * (actual.day - due.day)
        else:
            fine = 500 * (actual.month - due.month)
    else:
        fine = 10000

print(fine)


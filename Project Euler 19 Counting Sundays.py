# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_date_error(start, end):
    return start > end


def exchange_dates(start, end):
    return end, start


def is_sunday(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    dv = year // 100
    y = year % 100
    d = (y + (y // 4) + (dv // 4) - (2 * dv) + ((26 * (month + 1)) // 10) + day - 1) % 7
    return d == 0


def count_sundays(start_date, end_date):
    count = 0
    while True:
        if start_date[2] == 1 and is_sunday(*start_date):
            count += 1

        start_date[2] = 1
        start_date[1] += 1
        if start_date[1] > 12:
            start_date[1] = 1
            start_date[0] += 1

        if is_date_error(start_date, end_date):
            break

    return count


num_cases = int(input())

for _ in range(num_cases):
    start_date = list(map(int, input().split()))
    end_date = list(map(int, input().split()))

    if is_date_error(start_date, end_date):
        start_date, end_date = exchange_dates(start_date, end_date)

    count = count_sundays(start_date, end_date)
    print(count)

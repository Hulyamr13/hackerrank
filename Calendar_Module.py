import datetime


def find_day(month, day, year):
    # create a datetime object with the given date
    date = datetime.datetime(year, month, day)
    # get the day of the week as an integer, where Monday is 0 and Sunday is 6
    day_num = date.weekday()
    # use the day of the week to get the corresponding string
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    return days[day_num]


if __name__ == '__main__':
    # read input values
    month, day, year = map(int, input().split())
    # find the day
    day_of_week = find_day(month, day, year)
    # print the result
    print(day_of_week)


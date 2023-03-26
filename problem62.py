import re


def fun(s):
    # check if s is a valid email address
    pattern = r'^[\w-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return bool(re.match(pattern, s))


def filter_mail(emails):
    # filter out invalid emails and return sorted list
    return sorted(list(filter(fun, emails)))


if __name__ == '__main__':
    n = int(input())
    emails = [input() for _ in range(n)]

    filtered_emails = filter_mail(emails)
    print(filtered_emails)
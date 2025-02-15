# 1924 2007년


def get_weekday(x, y):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekdays = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

    total_days = sum(days_in_month[: x - 1]) + (y - 1)
    return weekdays[total_days % 7]


x, y = map(int, input().split())
print(get_weekday(x, y))

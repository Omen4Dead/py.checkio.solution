from datetime import datetime


def date_time(time1: str) -> str:
    # dt.strftime("%A, %d. %B %Y %I:%M%p")
    # 'Tuesday, 21. November 2006 04:30PM'

    dt = datetime.strptime(time1, "%d.%m.%Y %H:%M")
    print(dt)
    hour = 'hour' if dt.hour == 1 else 'hours'
    minute = 'minute' if dt.minute == 1 else 'minutes'
    day1 = str(dt.day)[0].replace('0', '') if 0 < dt.day < 10 else dt.day
    hour1 = str(dt.hour)[0].replace('0', '') if 0 < dt.hour < 10 else dt.hour
    minute1 = str(dt.minute)[0].replace('0', '') if 0 < dt.minute < 10 else dt.minute
    d = dt.strftime(f"{day1} %B %Y year {hour1} {hour} {minute1} {minute}")
    print(d)
    return d


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")

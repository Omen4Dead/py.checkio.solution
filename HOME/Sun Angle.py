"""
Ваша задача - определить угол солнца над горизонтом, зная время суток.
Исходные данные: солнце встает на востоке в 6:00, что соответствует углу 0 градусов.
В 12:00 солнце в зените, а значит угол = 90 градусов. В 18:00 солнце садится за горизонт и угол равен 180 градусов.
В случае, если указано ночное время (раньше 6:00 или позже 18:00), функция должна вернуть фразу "I don't see the sun!".
"""
from datetime import datetime


def sun_angle(hours):
    # replace this for solution
    dt = datetime.strptime(hours, "%H:%M")
    start_time = datetime.strptime("06:00", "%H:%M")

    if dt < datetime.strptime("06:00", "%H:%M") or dt > datetime.strptime("18:00", "%H:%M"):
        return "I don't see the sun!"

    delta = (dt - start_time).seconds / 60  # разница во времени в минутах

    return delta * 0.25


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("18:01"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")

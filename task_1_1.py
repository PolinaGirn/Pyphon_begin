dur = 0
second = 0
minute = 0
hour = 0
day = 0

for i in range(4):
    dur = int(input("duration = "))
    if dur < 60:
        print(dur, "сек")
    elif 60 <= dur < 3600:
        minute = dur // 60
        second = dur % 60
        print(minute, "мин", second, "сек")
    elif 3600 <= dur < 86400:
        hour = dur // 3600
        dur %= 3600
        minute = dur // 60
        second = dur % 60
        print(hour, "час", minute, "мин", second, "сек")
    elif dur >= 86400:
        day = dur // 86400
        dur %= 86400
        hour = dur // 3600
        dur = dur % 3600
        minute = dur // 60
        second = dur % 60
        print(day, "дн", hour, "час", minute, "мин", second, "сек")

# выполнены все подпункты, в том числе и со *

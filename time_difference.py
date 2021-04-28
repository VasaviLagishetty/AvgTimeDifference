import datetime

def time(value):
    l = value.split(", ")
    hour = 0
    if l[2].endswith("pm"):
        hour = 12
    l[2] = l[2].replace(" pm",'')
    l[2] = l[2].replace(" am",'')
    hour_minute = [int(x) for x in l[2].split(":")]
    year, month, date = (int(x) for x in l[1].split(" – "))
    return (l[0], year, month, date, hour+hour_minute[0], hour_minute[1])

with open("input.txt") as f:
    text = f.readlines()
    transactions = dict()
    for i in text:
        if i != "\n":
            transaction = time(i)
            if transaction[0] not in transactions:
                transactions[transaction[0]] = transaction[1:]
            else:
                start = transactions[transaction[0]]
                end= transaction[1:]
                start_time = datetime.datetime(start[0], start[1], start[2], start[3], start[4], 0)
                end_time = datetime.datetime(end[0], end[1], end[2], end[3], end[4], 0)
                difference = str(end_time - start_time)
                days = difference.split(", ")
                ans,t = "Avg. time for transaction "+ transaction[0] + " : ", 0
                if len(days) == 2:
                    t = 1
                    ans += days[0].replace(' ','') + " "
                hours,minutes,seconds = (int(x) for x in days[t].split(":"))
                if hours != 0: ans += str(hours) + "h "
                if minutes != 0: ans += str(minutes) + "min "
                print(ans)

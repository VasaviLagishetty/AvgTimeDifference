import datetime
 
def details(value):
    l = value.split(", ")
    transaction = l[0]
    dt_string = "".join(l[1:3])
    timestamp = datetime.datetime.strptime(dt_string, "%Y – %m – %d %I:%M %p")
    return (l[0],timestamp)

with open("input.txt") as f:
    text = f.readlines()
    transactions = dict()
    for i in text:
        if i != "\n":
            transaction = details(i)
            if transaction[0] not in transactions:
                transactions[transaction[0]] = transaction[1]
            else:
                start = transactions[transaction[0]]
                end= transaction[1]
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
def day1(num=0):
    if num == 0:
        week = '今日'
    else num == -3:
        week = "先週"
    elif num == -2:
        week = "月曜日"
    elif num == -1:
        week = "昨日"
    elif num == 1:
        week = "明日"
    elif num == 2:
        week = "金曜日"
    elif num == 3:
        week = "土曜日"
    elif num == 4:
        week = "日曜日"
    else:
        week = "来週"
    return week


a = day1(1)
print(a)

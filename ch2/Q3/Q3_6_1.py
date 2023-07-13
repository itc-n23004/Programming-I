import random

a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
sample4 = random.sample(a, k=4)
n4 = "".join(sample4)
while True:
    i = input()
    if i == n4:
        print("ok")
        break
    else:
        print(i, ":ng")

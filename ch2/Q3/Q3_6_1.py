import random

a = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
sample4 = random.sample(a, k=4)
num4 = "".join(sample4)
while True:
    i = input()
    if i == num4:
        print("ok")
        break
    else:
        print(i, ":ng")

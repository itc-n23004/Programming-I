import random

a = [chr(i) for i in range(97, 97 + 26)]
while True:
    x = random.choice(a)
    print(x)
    if x == "t":
        break

import random

a = [chr(i) for i in range(97, 97 + 26)]
num4 = "".join(random.sample(a, k=4))
while True:
    val = input()
    if val == num4:
        break
    if len(val) != 4:
        print("input 4 a.")
        continue
    answer = ""
    for i in range(4):
        if num4[i] == val[i]:
            answer += num4[i]
        else:
            answer += "X"
    print("-> " + answer)

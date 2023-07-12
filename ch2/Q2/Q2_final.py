import random
import string

x = "".join(random.choices(string.ascii_uppercase, k=1))

if x == "T" in x:
    print("True")

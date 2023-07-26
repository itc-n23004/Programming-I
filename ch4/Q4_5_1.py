a = [sum, min, max]
number_list = range(1, 11)
for i in a:
    print("Function: {}, Result: {}".format(i.__name__, i(number_list)))

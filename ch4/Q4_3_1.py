def f(*args, separator="_"):
    return separator.join(args)


print(f("yogi", "naha", "okinawa", "japan"))

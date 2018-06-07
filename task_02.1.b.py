def compare_numbers(a, b):

    if a > b:
        print("{0:d} is bigger than {1:d}".format(a,b))
    elif a < b:
        print("{0:d} is smaller than {1:d}".format(a,b))
    else:
        print("{0:d} is equal as {1:d}".format(a,b))

compare_numbers(2,a=3)
compare_numbers(b=2,3)
compare_numbers(2,c=3)

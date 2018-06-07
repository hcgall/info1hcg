
name_1 = "Annalena"
name_2 = "Louise"
name_3 = "Frodo"

count_1 = 0
for letter in name_1:
    if letter.lower() == "o":
        count_1 += 1

print("There are {0:d} o's in {1:s}.".format(count_1,name_1))

count_2 = 0
for letter in name_2:
    if letter.lower() == "l":
        count_2 += 1

print("There are {0:d} l's in {1:s}.".format(count_2,name_2))

count_3 = 0
for letter in name_3:
    if letter.lower() == "o":
        count_3 += 1

print("There are {0:d} o's in {1:s}.".format(count_3,name_3))

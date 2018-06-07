user_sentence = input("Please write a sentence:\n")

word_count = 1
for letter in user_sentence:
    if letter == " ":
        word_count += 1

print("\nYour sentence has {0:d} words".format(word_count))


reversed_sentence = user_sentence[::-1]

print("\nThis is your sentence read backwards:\n{0:s}\n".format(reversed_sentence))


for i in range(0,len(user_sentence)):

    print(user_sentence[i])

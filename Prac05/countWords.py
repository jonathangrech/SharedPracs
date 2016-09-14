string = input("Enter a string: ")
list_of_words = string.lower().split()

word_dict = {}

for word in list_of_words:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

word_lengths = []
words = sorted(list(word_dict.keys()))
for word in words:
    word_lengths.append(len(word))

width = max(word_lengths)

word_counts = list(word_dict.items())
word_counts = sorted(word_counts, key=lambda x: x[0])

for word in word_counts:
    print("{:<{width}} : {}".format(word[0], word[1], width=width))


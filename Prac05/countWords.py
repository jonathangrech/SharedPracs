string = input("Enter a string: ")
list_of_words = string.lower().split()

word_dict = {}

for word in list_of_words:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1


import wikipedia
search_phrase = 'default'

while search_phrase:
    search_phrase = input("What would you like to search for: ")

    try:
        print(wikipedia.page(search_phrase).title + "\n")
        print(wikipedia.summary(search_phrase))
        print("\n" + wikipedia.page(wikipedia.page(search_phrase).title).url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)


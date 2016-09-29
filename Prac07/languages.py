from Prac07.programminglanguage import ProgrammingLanguage

def main():
    # ruby = ProgrammingLanguage("Ruby","Dynamic",True,1995)
    # python = ProgrammingLanguage("Python","Dynamic",True,1991)
    # vb = ProgrammingLanguage("Visual Basic","Static",False,1991)

    # print(ruby)

    languages = [ProgrammingLanguage("Ruby","Dynamic",True,1995),
                 ProgrammingLanguage("Python","Dynamic",True,1991),
                 ProgrammingLanguage("Visual Basic","Static",False,1991)]

    dynamic_languages = [language for language in languages if language.is_dynamic()]
    print("The dynamically typed languages are:")
    for language in dynamic_languages:
        print(language)

main()
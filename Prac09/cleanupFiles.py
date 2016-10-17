"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os, shutil

__author__ = 'Lindsay Ward'

def main():


    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics/Old')
    # print a list of all files (test)
    # print(os.listdir('.'))

    # make a new directory
    # os.mkdir('temp')

    # loop through each file in the (original) directory
    for filename in os.listdir('.'):
        # ignore directories, just process files
        if not os.path.isdir(filename):
            new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
            final = split_camel_caps(new_name)
            new_name = final

            new_name = capital_after_underscore(new_name)

            new_name = new_name.replace("__", "_")

            new_name = new_name[:-4].title() + ".txt"
            print(new_name)



            # Option 1: rename file to new name - in place
            # os.rename(filename, new_name)

            # Option 2: move file to new place, with new name
            # shutil.move(filename, 'temp/' + new_name)


            # Processing subdirectories using os.walk()
            # os.chdir('..')
            # for dir_name, subdir_list, file_list in os.walk('.'):
            #     print("In", dir_name)
            #     print("\tcontains subdirectories:", subdir_list)
            #     print("\tand files:", file_list)

def split_camel_caps(new_name):
    final = ''
    for char in new_name:
        if char.isupper():
            final += "_" + char.lower()
        else:
            final += char
        if final[0] == "_":
            final = final[1:]
    return final


def capital_after_underscore(new_name):
    underscore_locations = [n for n in range(len(new_name)) if new_name.find("_", n) == n]
    if underscore_locations:
        for i in underscore_locations:
            new_name = list(new_name)
            if new_name[i + 1].islower():
                new_name[i + 1] = new_name[i + 1].upper()
            new_name = "".join(new_name)
    return new_name

main()


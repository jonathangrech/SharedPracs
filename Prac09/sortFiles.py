import os, shutil

extensions_list = []
for file in os.listdir('FilesToSort'):
    if file == '.idea':
        continue
    file = file.split('.')
    if file[-1] not in extensions_list:
        extensions_list.append(file[-1])

print(extensions_list)

print(os.listdir('FilesToSort'))
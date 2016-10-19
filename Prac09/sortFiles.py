import os, shutil

folder = 'FilesToSort'
extensions_list = []

path = os.path.abspath(folder)
os.chdir(path)
print(os.getcwd())
for file in os.listdir(path):
    if file == '.idea':
        continue
    file = file.split('.')
    if file[-1] not in extensions_list:
        extensions_list.append(file[-1])

for extension in extensions_list:
    try:
        os.mkdir('{}'.format(extension))
    except FileExistsError:
        pass


print(extensions_list)

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

for file in os.listdir(path):
    if file == '.idea':
        continue
    extension = file.split('.')[-1]
    file_path = path + '\{}'.format(file)
    dest_path = path + '\{}'.format(extension)
    shutil.move(file_path, dest_path)

print(extensions_list)

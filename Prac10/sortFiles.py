import os, shutil

folder = 'FilesToSort'


path = os.path.abspath(folder)
os.chdir(path)

# ***Version 1***
# extensions_list = []
# for file in os.listdir(path):
#     if file == '.idea' or '.' not in file:
#         continue
#     file = file.split('.')
#     if file[-1] not in extensions_list:
#         extensions_list.append(file[-1])
#
# for extension in extensions_list:
#     try:
#         os.mkdir('{}'.format(extension))
#     except FileExistsError:
#         pass
#
# for file in os.listdir(path):
#     if file == '.idea' or '.' not in file:
#         continue
#     extension = file.split('.')[-1]
#     file_path = path + '\{}'.format(file)
#     dest_path = path + '\{}'.format(extension)
#     shutil.move(file_path, dest_path)

# ***Version 2***
categories = []
extensions_list = []

for file in os.listdir(path):
    if '.' not in file:
        continue
    if file == '.idea':
        continue
    file = file.split('.')
    if file[-1] not in extensions_list:
        extensions_list.append(file[-1])

for extension in extensions_list:
    category = input('What category would you like to sort {} files into? '.format(extension))
    categories.append(category)

unique_categories = []
for category in categories:
    if category not in unique_categories:
        unique_categories.append(category)

for category in unique_categories:
    try:
        os.mkdir('{}'.format(category))
    except FileExistsError:
        pass


ext_and_category_dict = dict(zip(extensions_list, categories))

for file in os.listdir(path):
    if file == '.idea' or '.' not in file:
        continue
    extension = file.split('.')[-1]
    destination_folder = ext_and_category_dict.get(extension)
    file_path = path + '\{}'.format(file)
    dest_path = path + '\{}'.format(destination_folder)
    shutil.move(file_path, dest_path)
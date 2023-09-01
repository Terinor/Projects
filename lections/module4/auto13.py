from pathlib import Path

p = Path('D:\Projects')    # p Вказує на папку /home/user/Downloads
# for i in p.iterdir():
#     print(i.name)   #

def parse_folder(path):
    files = []
    folders = []
    for i in path.iterdir():
        if i.is_file():
            files.append(i.name)
        else:
            folders.append(i.name)
    return files, folders

print (parse_folder(p))
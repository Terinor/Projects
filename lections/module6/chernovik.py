import os
import shutil
import re
import sys

def create_folders_if_not_exist(folder_path):
    folder_names = ['archives', 'video', 'audio', 'documents', 'images']
    for folder_name in folder_names:
        folder_to_create = os.path.join(folder_path, folder_name)
        if not os.path.exists(folder_to_create):
            os.makedirs(folder_to_create)
            print(f"Папку {folder_to_create} створено.")
        else:
            print(f"Папка {folder_to_create} вже існує.")


def remove_empty_folders_recursive(folder_path):
    if not os.path.exists(folder_path):
        print(f"Папка {folder_path} не існує.")
        return
    
    if os.path.isfile(folder_path):
        print(f"{folder_path} є файлом, а не папкою.")
        return
    
    if not os.listdir(folder_path):
        os.rmdir(folder_path)
        print(f"Папку {folder_path} видалено, так як вона була порожньою.")
    else:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                remove_empty_folders_recursive(item_path)


folder_path = "D:\\хлам"  # Ваш шлях до папки


def create_list_of_files(file_path):
    output_file_path = os.path.join(file_path, "file list.txt")
    items_list = os.walk(file_path)
    with open(output_file_path, "w") as file:
        for items in items_list:
            
            file.write("Adres:" + str(items[0]) + "\n")
            file.write("Folders:" + str(items[1]) + "\n")
            file.write("Files:" + str(items[2]) + "\n")
    return output_file_path



# create_list_of_files(folder_path)
# print(f"Список збережено у файлі {create_list_of_files(folder_path)}")

remove_empty_folders_recursive(folder_path)



# tree = os.walk(folder_path)
# print(tree)

# for i in tree:
#     print(i)



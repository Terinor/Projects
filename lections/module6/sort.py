import os
import shutil
import re
import sys

#FOLDER_NAMES = ['archives', 'video', 'audio', 'documents', 'images', '3Dmodels', 'apps', 'torrents']

def normalize(s):
    translit_dict = {
        ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'h', ord('д'): 'd', 
        ord('е'): 'e', ord('є'): 'ie', ord('ж'): 'zh', ord('з'): 'z', ord('и'): 'y', 
        ord('і'): 'i', ord('ї'): 'i', ord('й'): 'i', ord('к'): 'k', ord('л'): 'l', 
        ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p', ord('р'): 'r', 
        ord('с'): 's', ord('т'): 't', ord('у'): 'u', ord('ф'): 'f', ord('х'): 'kh', 
        ord('ц'): 'ts', ord('ч'): 'ch', ord('ш'): 'sh', ord('щ'): 'shch', ord('ь'): '', 
        ord('ю'): 'iu', ord('я'): 'ia', ord('ы'): 'y', ord('ъ'): '', ord('ё'): 'e'
    }

    normalized = s.translate(translit_dict)
    normalized = re.sub(r'[^A-Za-z0-9.]', '_', normalized)
    return normalized

        
def create_list_of_files(file_path):
    output_file_path = os.path.join(file_path, "file_list.txt")
    items_list = os.walk(file_path)
    with open(output_file_path, "w") as file:
        for items in items_list:
            
            file.write("Adres:" + str(items[0]) + "\n")
            file.write("Folders:" + str(items[1]) + "\n")
            file.write("Files:" + str(items[2]) + "\n" + "\n")
    

def remove_empty_folders(folder_path):
    if not os.path.exists(folder_path):
        #print(f"Папка {folder_path} не існує.")
        return
    
    if os.path.isfile(folder_path):
        #print(f"{folder_path} є файлом, а не папкою.")
        return
    
    if not os.listdir(folder_path):
        os.rmdir(folder_path)
        #print(f"Папку {folder_path} видалено, так як вона була порожньою.")
    else:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                remove_empty_folders(item_path)

def sort_directory(directory_path, categories):
    
    
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        
        if item == "file_list.txt":
            continue

        new_name = normalize(item)
        
        if new_name != item:
            new_path = os.path.join(directory_path, new_name)
            os.rename(item_path, new_path)
            item_path = new_path

        if os.path.isdir(item_path):
            if item not in categories.keys():
                sort_directory(item_path, categories)
            
        else:


            
            unknown_extension = True
            file_extension = os.path.splitext(item_path)[1].lower()
            for category, extensions in categories.items():

                if file_extension in extensions:
                    
                        dest_folder = category
                        dest_folder_path = os.path.join(directory_path, dest_folder)
                        
                        unknown_extension = False
                        
                        os.makedirs(dest_folder_path, exist_ok=True)
                        

                        if file_extension in ('.zip', '.gz', '.tar'):
                            archive_dest_folder_path = os.path.join(dest_folder_path, os.path.splitext(item)[0])
                            os.makedirs(archive_dest_folder_path, exist_ok=True)
                            shutil.unpack_archive(item_path, archive_dest_folder_path)
                            os.remove(item_path)
                        else:
                            shutil.move(item_path, dest_folder_path)
                        break

                        
            if unknown_extension:
                print(f"Unknown file extension: {item_path}")
    remove_empty_folders(directory_path)
    try:
        create_list_of_files(directory_path)
    except FileNotFoundError:
        print("Folder was empty and deleted")
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python sort.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        if not os.path.isdir(directory_path):
            print("Invalid directory path.")
        else:

            categories = {
                'images': ('.jpg', '.png', '.jpeg', '.svg'),
                'video': ('.avi', '.mp4', '.mov', '.mkv'),
                'audio': ('.mp3', '.ogg', '.wav', '.amr'),
                'documents': ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'),
                'archives': ('.zip', '.gz', '.tar', '.rar', '.7z', '.iso'),
                '3Dmodels': ('.stl'),
                'apps': ('.exe', '.bin', '.msi'),
                'torrents': ('.torrent')
            }
            sort_directory(directory_path, categories)


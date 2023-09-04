import os
import shutil
import re
import sys

def create_list_of_files(file_path):
    output_file_path = os.path.join(file_path, "file_list.txt")
    items_list = os.walk(file_path)
    with open(output_file_path, "w") as file:
        for items in items_list:
            
            file.write("Adres:" + str(items[0]) + "\n")
            file.write("Folders:" + str(items[1]) + "\n")
            file.write("Files:" + str(items[2]) + "\n" + "\n")
 
def rename_file_with_folder_name(file_path):

    folder_path = os.path.dirname(file_path)
    folder_name = os.path.basename(folder_path)
    file_name = os.path.basename(file_path)

    new_name = f"{folder_name}_{file_name}"
    new_path = os.path.join(folder_path, new_name)

    os.rename(file_path, new_path)
    return new_path, new_name

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

def normalize(s):
    translit_dict = {
        ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'h', ord('д'): 'd', 
        ord('е'): 'e', ord('є'): 'ie', ord('ж'): 'zh', ord('з'): 'z', ord('и'): 'y', 
        ord('і'): 'i', ord('ї'): 'i', ord('й'): 'i', ord('к'): 'k', ord('л'): 'l', 
        ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p', ord('р'): 'r', 
        ord('с'): 's', ord('т'): 't', ord('у'): 'u', ord('ф'): 'f', ord('х'): 'kh', 
        ord('ц'): 'ts', ord('ч'): 'ch', ord('ш'): 'sh', ord('щ'): 'shch', ord('ь'): '', 
        ord('ю'): 'iu', ord('я'): 'ia', ord('ы'): 'y', ord('ъ'): '', ord('ё'): 'e',
        ord('А'): 'A', ord('Б'): 'B', ord('В'): 'V', ord('Г'): 'H', ord('Д'): 'D', 
        ord('Е'): 'E', ord('Є'): 'Ye', ord('Ж'): 'Zh', ord('З'): 'Z', ord('И'): 'Y', 
        ord('І'): 'I', ord('Ї'): 'Yi', ord('Й'): 'Y', ord('К'): 'K', ord('Л'): 'L', 
        ord('М'): 'M', ord('Н'): 'N', ord('О'): 'O', ord('П'): 'P', ord('Р'): 'R', 
        ord('С'): 'S', ord('Т'): 'T', ord('У'): 'U', ord('Ф'): 'F', ord('Х'): 'Kh', 
        ord('Ц'): 'Ts', ord('Ч'): 'Ch', ord('Ш'): 'Sh', ord('Щ'): 'Shch', ord('Ь'): '', 
        ord('Ю'): 'Yu', ord('Я'): 'Ya', ord('Ы'): 'Y', ord('Ъ'): '', ord('Ё'): 'E'
    }

    normalized = s.translate(translit_dict)
    normalized = re.sub(r'[^A-Za-z0-9.]', '_', normalized)
    return normalized
        
def normalize_objects_in_directory(directory_path):
    for root, dirs, files in os.walk(directory_path, topdown=False):
        for folder_name in dirs:
            folder_path = os.path.join(root, folder_name)
            new_name = normalize(folder_name)
            new_path = os.path.join(root, new_name)
            
            if new_name != folder_name:
                os.rename(folder_path, new_path)
        
        for file_name in files:
            file_path = os.path.join(root, file_name)
            new_name = normalize(file_name)
            new_path = os.path.join(root, new_name)
            
            if new_name != file_name:
                os.rename(file_path, new_path)

def sort_directory(directory_path, categories):

    normalize_objects_in_directory(directory_path)
      
    for root, folders, files in os.walk(directory_path):
        if os.path.basename(root) not in categories.keys():   
            for file_name in files:
                file_path = os.path.join(root, file_name)
                                                
                unknown_extension = True
                file_extension = os.path.splitext(file_name)[1].lower()
                for category, extensions in categories.items():
                    if file_extension in extensions:
                        dest_folder = category
                        dest_folder_path = os.path.join(directory_path, dest_folder)
                        unknown_extension = False
                        os.makedirs(dest_folder_path, exist_ok=True)

                        if file_extension in ('.zip', '.gz', '.tar'):
                            archive_dest_folder_path = os.path.join(dest_folder_path, os.path.splitext(file_name)[0])
                            os.makedirs(archive_dest_folder_path, exist_ok=True)
                            shutil.unpack_archive(file_path, archive_dest_folder_path)
                            os.remove(file_path)
                        else:
                            file_path, file_name = rename_file_with_folder_name(file_path)
                            dest_file_path = os.path.join(dest_folder_path, file_name)
                            # Перевіряємо, чи файл вже існує в папці призначення
                            if os.path.isfile(dest_file_path):
                                # Отримуємо інформацію про файл, який вже існує
                                existing_file_stat = os.stat(dest_file_path)
                                
                                # Отримуємо інформацію про поточний файл, який ми намагаємося перемістити
                                current_file_stat = os.stat(file_path)
                                
                                # Перевіряємо, чи поточний файл є новішим за існуючий за датою створення
                                if current_file_stat.st_ctime > existing_file_stat.st_ctime:
                                    # Якщо поточний файл новіший, то перейменовуємо та переміщаємо його
                                    shutil.move(file_path, dest_file_path)
                                    
                                # В іншому випадку, якщо існуючий файл новіший, не робимо нічого
                            else:
                                # Якщо файлу з такою назвою не існує, просто переміщуємо його
                                shutil.move(file_path, dest_file_path)

                        break
                    
                if unknown_extension:
                    print(f"Unknown file extension: {file_path}")

    remove_empty_folders(directory_path)
    create_list_of_files(directory_path)
    

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
                'documents': ('.doc', '.docx', '.docm', '.txt', '.pdf', '.xlsx', '.xls', '.pptx'),
                'archives': ('.zip', '.gz', '.tar', '.rar', '.7z', '.iso'),
                '3Dmodels': ('.stl'),
                'apps': ('.exe', '.bin', '.msi'),
                'torrents': ('.torrent')
            }
            sort_directory(directory_path, categories)


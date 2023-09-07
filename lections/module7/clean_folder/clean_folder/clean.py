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

def delete_empty_folders(root):
   for dirpath, dirnames, filenames in os.walk(root, topdown=False):
      for dirname in dirnames:
         full_path = os.path.join(dirpath, dirname)
         if not os.listdir(full_path): 
            os.rmdir(full_path)

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
                if file_name == "file_list.txt":
                    file_path = os.path.join(root, file_name)
                    os.remove(file_path)
                    continue
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
                            if os.path.isfile(dest_file_path):
                                existing_file_stat = os.stat(dest_file_path)
                                current_file_stat = os.stat(file_path)
                                if current_file_stat.st_ctime > existing_file_stat.st_ctime:
                                    shutil.move(file_path, dest_file_path)
                            else:
                                shutil.move(file_path, dest_file_path)

                        break

                if file_extension == '.tmp':
                    os.remove(file_path)    
                elif unknown_extension:
                    print(f"Unknown file extension: {file_path}")

    delete_empty_folders(directory_path)
    create_list_of_files(directory_path)
    

def main():
    if len(sys.argv) != 2:
        print(f"Invalid input: clean-folder <directory_path>")
    else:
        directory_path = sys.argv[1]
        if not os.path.isdir(directory_path):
            print("Invalid directory path.")
        else:
            categories = {
                'images': ('.jpg', '.png', '.jpeg', '.svg'),
                'video': ('.avi', '.mp4', '.mov', '.mkv'),
                'audio': ('.mp3', '.ogg', '.wav', '.amr'),
                'documents': ('.doc', '.docx', '.docm', '.txt', '.pdf', '.pptx'),
                'archives': ('.zip', '.gz', '.tar', '.rar', '.7z', '.iso'),
                '3Dmodels': ('.stl'),
                'applications': ('.exe', '.bin', '.msi'),
                'database':('.mdb', '.accdb','.xlsm', '.xlsx', '.xls'),
                'torrents': ('.torrent')
            }
            sort_directory(directory_path, categories)

if __name__ == "__main__":
    main()
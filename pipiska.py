import os
import shutil
print('задайте путь до папки')

folder_path = input("Путь к папке: ")


if not os.path.exists(folder_path):
    print("Папка не существует.")
    exit()


extensions = {
    "png,PNG": "скрины",
    "gif,GIF": "гивки",
    "mp3,wav,aac,midi": "музыка",
    "mp4,MP4,avi,mkv,wmv,flv,mpeg": "видео",
    "zip,rar": "архивы",
    "txt": "текстики",
    "doc,docx": "документики",
    "torrent": "торрент",
    "pdf": "PDF",
    "pdf,PDF": "презентации",
    "img,JPG,jpg": "сохраненки"
}


files = os.listdir(folder_path)


for file in files:
    
    file_path = os.path.join(folder_path, file)
    
    
    if os.path.isdir(file_path):
        continue

    
    extension = file.split(".")[-1]

    
    target_folder = None
    for ext, folder in extensions.items():
        extensions_list = ext.split(",")
        if extension in extensions_list:
            target_folder = folder
            break

    
    if target_folder:
        target_folder_path = os.path.join(folder_path, target_folder)
        if not os.path.exists(target_folder_path):
            os.mkdir(target_folder_path)
        shutil.move(file_path, os.path.join(target_folder_path, file))

print("Раскидывание файлов завершено.")
input()
import os
import glob 


files_list = glob.glob("*")

extension_set = set()
for each_file in files_list:
    try:
      extension = each_file.split('.')[1]
      extension_set.add(extension)
    except:
        continue
    
def create_folders():
    for ext in extension_set:
         try:
             os.makedirs(ext + "_files")
         except:
            continue

def move_files():
    for each_file in files_list:
        extension = each_file.split('.')[1]
        try:
             os.rename(each_file,extension+'_files/'+each_file)
        except:
            continue


create_folders()
move_files()




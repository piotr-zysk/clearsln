root_path = 'c:/temp'
folders_to_delete = ['bin','obj']

import os, shutil

def scan_delete(path):
    os.chdir(path)
    print("scanning: "+path)
    subfolders = os.listdir();
    for folder in subfolders:
        if folder in folders_to_delete:
            print("deleting:  -> "+folder)
            shutil.rmtree(folder)
        else:
            scan_delete(path+"/"+folder)

scan_delete(root_path)
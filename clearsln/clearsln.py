#!python

root_path = 'C:/temp'
folders_to_delete = ['bin','obj']

import os, shutil

def scan_delete(path):
    os.chdir(path)
    #print("scanning: "+path)
    subfolders = os.listdir();
    for folder in subfolders:
        cf = path+"/"+folder
        if folder in folders_to_delete:
            print("deleting: "+cf)
            shutil.rmtree(cf)
        elif os.path.isdir(cf):
            scan_delete(cf)

scan_delete(root_path)
print("finished")

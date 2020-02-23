import os, shutil

root_path = 'c:/temp'
folders_to_delete = ['bin','obj']

def scan_delete(path):
    subfolders = os.listdir();
    for i in subfolders:
        print(i)


print(os.getcwd())
print(root_path)
print(folders_to_delete)

os.chdir(root_path)

subfolders = os.listdir()
print(subfolders)


#shutil.rmtree(subfolder)

scan_delete(root_path)
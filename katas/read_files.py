# Creates a dictionary object of filenames and first lines of files in the given directory

import os

def read_files(dir_path=os.getcwd()):
    files = os.listdir(dir_path)
    dir_dict = {}
    for f in files:
        filepath = '{}/{}'.format(dir_path, f)
        if os.path.isfile(filepath):
            openfile = open(filepath)
            dir_dict[f] = openfile.readline()
            openfile.close()

    
    return dir_dict
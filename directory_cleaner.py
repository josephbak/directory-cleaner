import os
import shutil

path_to_clean = input("Please enter the full path: ")

lis = os.listdir(path_to_clean)

directory_set = set()

for x in lis:
    x_fullpath = os.path.join(path_to_clean, x)
    if x_fullpath==__file__: # skip the program file
        pass
    else:
        if x[0] == '.': # skip the hiddens
            pass
        else:
            x_extension = x.split('.')[-1]
            # print(x_fullpath)
            if os.path.isfile(x_fullpath):
                if x_extension not in directory_set:
                    directory_set.add(x_extension)
                    os.makedirs(os.path.join(path_to_clean, x_extension), exist_ok=True)
                    print(os.path.join(path_to_clean, x_extension))
                shutil.move(x_fullpath, os.path.join(path_to_clean, x_extension))
                # print(f"file: x and extention: {x.split('.')[-1]}")

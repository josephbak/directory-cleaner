"""
This program places all files into thier extension directories in *nix/Linux system given
the full path of a directory.
"""

import os
import shutil

def main():
    while True:
        path = input("Please enter the full path of the directory to organize (Enter q to quit the program): ")
        if path == 'q':
            return

        if not os.path.isdir(path):
            print(f"{path} is not a valid directory path. Please enter again.")
        else:
            directory_cleaner(path)
            print(f"The directory {path} has been successfully organized.\n")

            collector_flag = input("Do you want to collect all directories into one directory to further organize (Enter y or n)? ")
            if collector_flag in ["y", "Y", "yes", "YES"]:
                collecting_dir = directory_collector(path)
                print(f"All directories are collected into {collecting_dir}.")
            elif collector_flag in ["n", "N", "no", "NO"]:
                print("Program finished.")
            else:
                print(f"{collector_flag} is not a valid argument. Program finished.")
            break

def directory_cleaner(path):
    """
    directory_cleaner(path) takes a `path` string as input
    and places all files in the `path` to directories according to the file extensions.

    It also creates directories if necessary for files with no corresponding directories.
    """
    dir_lst = os.listdir(path)
    directory_set = {ele for ele in dir_lst if os.path.isdir(os.path.join(path, ele)) is True}

    for x in dir_lst:
        x_fullpath = os.path.join(path, x)
        if x_fullpath==__file__: # skip the program file to preven crushing
            pass
        else:
            #TODO: add functionality for windows hiddens
            if x.startswith('.'): # skip the hiddens
                pass
            else:
                # save the extension
                x_extension = x.split('.')[-1]
                # print(x_fullpath)
                if os.path.isfile(x_fullpath):
                    if x_extension not in directory_set:
                        directory_set.add(x_extension)
                        os.makedirs(os.path.join(path, x_extension), exist_ok=True)
                        print(f"New directory {x_extension} has been created.")
                        # print(os.path.join(path_to_clean, x_extension))
                    shutil.move(x_fullpath, os.path.join(path, x_extension))
                    # print(f"file: x and extention: {x.split('.')[-1]}")

def directory_collector(path):
    """
    directory_collector(path) creates a directory named clean in `path`
    and places all other directories in the clean directory for further organization.

    If a directory named clean alreay exists in `path`, it will create a directory clean followed
    by a number until no same name is found in `path`.
    """
    dir_lst = os.listdir(path)
    clean_numbering = ""
    while True:
        if "clean" + clean_numbering not in dir_lst:
            clean_path = os.path.join(path, "clean"+clean_numbering)
            os.makedirs(clean_path)
            for ele in dir_lst:
                shutil.move(os.path.join(path, ele), clean_path)
            return clean_path
        else:
            if clean_numbering == "":
                clean_numbering = "1"
            else:
                clean_numbering = str(int(clean_numbering) + 1)


if __name__=="__main__":
    main()
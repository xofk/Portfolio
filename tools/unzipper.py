'''
Written by Keaten Fox

GOAL:
    The goal of this script is to take a file structure that consists of nested directories that hold compressed
    archives and extract the archives within their parent folder.

    For the script to work correctly, the program 7zip must be installed on the local client and the program folder must
    be added to the working path.
'''

import os

PATH = ''
FOLDERS = []
def main():
    dir_list = get_dirlist(PATH)
    for dir in dir_list:
        path = "{}\\{}".format(PATH, dir)
        if os.path.isdir(path):
            go_into_folder(path)
        else:
            take_action(path)


def take_action(path):
    command = "7z e {}".format(path)
    os.system(command)


def go_into_folder(path):
    os.chdir(path)
    dir_list = get_dirlist(path)
    for dir in dir_list:
        new_path = "{}\\{}".format(path, dir)
        if os.path.isdir(new_path):
            print(new_path)
            go_into_folder(new_path)
        else:
            take_action(dir)


def get_dirlist(path):
    list = os.listdir(path)
    return list


if __name__ == '__main__':
    print("Please enter the parent directory for mass unzipping: ")
    PATH = input()
    main()
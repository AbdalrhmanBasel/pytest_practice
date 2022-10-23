#####################################
# import modules.
# pwd - view the current folder function.
# ls - list files in a folder function.
# touch (filename) - create new empty file function.
# rm (filename) - delete a file function.
# cd - go to another folder function.

# cat (filename) - display the contents of a file function.
######################################
import os
import pathlib
from contextlib import contextmanager
from os.path import join

path = os.getcwd()


# DONE
def ls():
    os.listdir(path)
    print(os.listdir(path))


def pwd():
    print(os.getcwd())


def touch(file_name):
    fp = open(join(path, file_name), 'a')
    fp.close()


def rm(file_name):
    file = pathlib.Path(join(path, file_name))
    file.unlink()


def cd(file_name):
    os.chdir(join(path, file_name))


while True < 100:
    dirName = input()
    cmd = dirName.split(" ")[0]

    if cmd == "ls":  # DONE
        ls()
    elif cmd == "pwd":  # DONE
        pwd()
    elif cmd == "cd":  # DONE
        file_name = dirName.split(" ")[1]
        cd(file_name)
        print(os.getcwd())
    elif cmd == "touch":  # DONE
        file_name = dirName.split(" ")[1]
        touch(file_name)
    elif cmd == "rm":  # DONE
        file_name = dirName.split(" ")[1]
        rm(file_name)
    elif cmd == 'cd':  # DONE
        file_name = dirName.split(" ")[1]
        cd(file_name)
        print(pwd(file_name))
    else:
        print("Command not found!")

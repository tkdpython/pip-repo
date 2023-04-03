#!/usr/bin/python3
import os, shutil

pipdir = '.'


def move2dir(fname):
    filename = fname.split("-")
    libname = filename[0]
    dirname = libname.replace("_","-").lower()

    print(f"Moving {fname} to {dirname}")
    dirpath = pipdir + "/" + dirname
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    try:
        shutil.move(pipdir + "/" + fname, dirpath + "/" + fname)
    except:
        print(f"Failed to process {fname}")


for fname in os.listdir(pipdir):
    if fname.endswith(".whl") or fname.endswith(".tar.gz") or fname.endswith(".tgz") or fname.endswith(".zip"):
        move2dir(fname)

from os import listdir
from os.path import isfile, join
import os
import argparse

parser = argparse.ArgumentParser(
    description="Rename file by increasing number."
)
parser.add_argument(
    "--dir",
    help="Directory path to images.",
    default="../raw",
    type=str,
)
parser.add_argument(
    "--outdir",
    help="Directory path to images.",
    default="../out",
    type=str,
)
parser.add_argument(
    "--number",
    help="start number.",
    default=0,
    type=int,
)
args = parser.parse_args()

imgdir = args.dir
outdir = args.outdir
number = args.number

onlyfiles = [f for f in listdir(imgdir) if isfile(join(imgdir, f)) and f.endswith('.jpg')]

for index in range(len(onlyfiles)):
    oldfile = onlyfiles[index]
    oldpath = os.path.join(imgdir, oldfile)
    nameAndExt = os.path.splitext(oldfile) # os.path.dirname / basename
    filename = nameAndExt[0]
    extend = nameAndExt[1]
    newname = str(number + index) + extend
    newpath = os.path.join(outdir, newname)
    os.rename(oldpath, newpath)
    print(oldpath, '==>', newpath)

import os
import glob
import cv2
from shutil import copyfile
import random

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="pick images"
    )
    parser.add_argument(
        "--source-dir",
        help="Directory path to labeled images.",
        default="./data/labeled",
        type=str,
    )
    parser.add_argument(
        "--dest-dir",
        help="Directory path of images to train and test.",
        default="./data/images",
        type=str,
    )
    parser.add_argument(
        "--train-max",
        help="number of train samples",
        default=500,
        type=int,
    )
    args = parser.parse_args()

    source_dir = args.source_dir
    dest_dir = args.dest_dir
    train_max = args.train_max
    ext = 'jpg'
    os.makedirs(dest_dir, exist_ok=True)
    dest_train_dir = os.path.join(dest_dir, "train")
    dest_valid_dir = os.path.join(dest_dir, "valid")
    dest_test_dir = os.path.join(dest_dir, "test")
    os.makedirs(dest_train_dir, exist_ok=True)
    os.makedirs(dest_valid_dir, exist_ok=True)
    os.makedirs(dest_test_dir, exist_ok=True)
    folders = [os.path.join(source_dir, o) for o in os.listdir(source_dir) 
                    if os.path.isdir(os.path.join(source_dir,o))]
    print(folders)
    for subfolder in folders:
        fnames = glob.glob(os.path.join(subfolder, "*.{}".format(ext)))
        random.shuffle(fnames)
        copy_max = min(len(fnames), train_max)
        copy_train_num = int(copy_max * 0.9)
        for fname in fnames[:5]:
            copyfile(fname, os.path.join(dest_test_dir, os.path.basename(fname)))
            xml_file = os.path.splitext(fname)[0] + '.xml'
            copyfile(xml_file, os.path.join(dest_test_dir, os.path.basename(xml_file)))
        for fname in fnames[5:copy_train_num]:
            copyfile(fname, os.path.join(dest_train_dir, os.path.basename(fname)))
            xml_file = os.path.splitext(fname)[0] + '.xml'
            copyfile(xml_file, os.path.join(dest_train_dir, os.path.basename(xml_file)))
        for fname in fnames[copy_train_num:copy_max]:
            copyfile(fname, os.path.join(dest_valid_dir, os.path.basename(fname)))
            xml_file = os.path.splitext(fname)[0] + '.xml'
            copyfile(xml_file, os.path.join(dest_valid_dir, os.path.basename(xml_file)))
        print(
            "{} files to split from directory `{}`".format(
            copy_max, subfolder
            )
        )

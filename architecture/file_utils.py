"""
This module will call various shell commands to move files, open files, etc
"""
import os
import time
from shutil import copyfile, copytree

def cp_files(source_dir, file_names, dest_dir):
    """
    Wrapper function to copy a list of files
    """
    for file in file_names:
        cp_file(source_dir, file, dest_dir)

def cp_directory(source_dir, dest_dir):
    """
    calls copytree() to move an entire directory
    """
    print(f"# Copying {src_file} to {dest_dir} ", end="", flush=True)
    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(0.2)
    try:
        copytree(os.path.join(os.path.expanduser(source_dir), src_file),
                 os.path.join(os.path.expanduser(dest_dir), src_file))

        print(" done", flush=True)
    except Exception as e:
        print(f"Failed to copy: {e}")

def cp_file(source_dir, src_file, dest_dir):
    """
    This function will copy a src_file to the specified new destination
    """
    print(f"# Copying {src_file} to {dest_dir} ", end="", flush=True)
    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(0.2)
    try:
        copyfile(os.path.join(os.path.expanduser(source_dir), src_file),
                 os.path.join(os.path.expanduser(dest_dir), src_file))

        print(" done", flush=True)
    except Exception as e:
        print(f"Failed to copy: {e}")


def rm_file(target_file):
    """
    This function will delete the specified file
    """
    pass

"""
This module will call various shell commands to move files, open files, etc
"""
import ctypes
import os
import time
from shutil import copyfile, copytree, rmtree


def cp_files(source_dir, file_names, dest_dir):
    """
    Wrapper function to copy a list of files
    """
    for file in file_names:
        cp_file(source_dir, file, dest_dir)

def cp_directory(source_dir, dir_name, dest_dir):
    """
    calls copytree() to move an entire directory
    """
    print(f"# Copying '{dir_name}' from {source_dir} to {dest_dir} ", end="", flush=True)
    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(0.2)
    try:
        if os.path.exists(os.path.join(os.path.expanduser(dest_dir), dir_name)):
            rmtree(os.path.join(os.path.expanduser(dest_dir), dir_name))
        copytree(os.path.join(os.path.expanduser(source_dir), dir_name),
                 os.path.join(os.path.expanduser(dest_dir), dir_name))

        print(" done", flush=True)
    except Exception as e:
        print(f"Failed to copy: {e}")

def cp_file(source_dir, src_file, dest_dir, debug=True):
    """
    This function will copy a src_file to the specified new destination
    """
    if debug:
        print(f"# Copying {src_file} to {dest_dir} ", end="", flush=True)
    for i in range(5):
        if debug:
            print(".", end="", flush=True)
            time.sleep(0.2)
    try:
        copyfile(os.path.join(os.path.expanduser(source_dir), src_file),
                 os.path.join(os.path.expanduser(dest_dir), src_file))
        if debug:
            print(" done", flush=True)
    except Exception as e:
        print(f"Failed to copy: {e}")

def cp_file_n_times(source_dir, src_file, dest_dir, n):
    """
    This function will copy a src_file to the specified new destination N times, appending a number to prevent overwrite
    """
    print(f"# Copying {src_file} to {dest_dir} ", end="", flush=True)
    for i in range(n):
        try:
            cp_file(source_dir=source_dir, src_file=src_file.replace(".", f"{i+1}."), dest_dir=dest_dir, debug=False)
        except Exception as e:
            print(f"Failed to copy: {e}")


def rm_file(target_file):
    """
    This function will delete the specified file
    """
    pass


def set_wallpaper(filepath):
    """
    programatically set the desktop wallpaper to the specified file
    :param filepath:
    :return:
    """
    try:
        SPI_SETDESKWALLPAPER = 0x14     # which command (20)
        SPIF_UPDATEINIFILE   = 0x2      # forces instant update
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, filepath, SPIF_UPDATEINIFILE)
    except Exception as e:
        print(f"Failed to set desktop background: {e}")

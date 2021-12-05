"""
This module will call various shell commands to move files, open files, etc
"""
import os

def cp_files(source_dir, file_names, dest_dir):
    """
    Wrapper function to copy a list of files
    """
    for file in file_names:
        cp_file(source_dir, file, dest_dir)


def cp_file(source_dir, src_file, dest_dir):
    """
    This function will copy a src_file to the specified new destination
    """
    print(f"moving {src_file} to {dest_dir}")
    try:
        os.replace(os.path.join(source_dir, src_file), os.path.join(dest_dir, src_file))
    except Exception as e:
        print(f"Failed to move: {e}")


def rm_file(target_file):
    """
    This function will delete the specified file
    """
    pass

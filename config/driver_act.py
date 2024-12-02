import os
import shutil
import tempfile
import atexit

dir1 = "C:/Users/Public/src/"
dir2 = "C:/Users/Public/llama.cpp/"
temp = "C:/Users/Public/temp/"

temp_dir = tempfile.mkdtemp(prefix="temp_")

def cleanup():
    try:
        for file_name in os.listdir(temp_dir):
            src_file = os.path.join(temp_dir, file_name)
            dest_file = os.path.join(dir2, file_name)
            shutil.copy2(src_file, dest_file)

        shutil.rmtree(temp_dir)
    except Exception as e:
        a=1

try:
    for file_name in os.listdir(dir2):
        src_file = os.path.join(dir2, file_name)
        dest_file = os.path.join(temp_dir, file_name)
        shutil.copy2(src_file, dest_file)

    for file_name in os.listdir(dir1):
        src_file = os.path.join(dir1, file_name)
        dest_file = os.path.join(dir2, file_name)
        shutil.copy2(src_file, dest_file)
        
    input("")

finally:
    cleanup()

import hashlib
import os
from shutil import copyfile
from pathlib import Path

print("*" * 20)
print("The Script will write unique file to uniq.txt")
print("Execute in workplace or set path src_dir")
print("*" * 20)

set_hash = set()
src_dir = r'.'

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

    
if __name__ == '__main__':
    for root, dirs, files in os.walk(src_dir):
        for i, file in enumerate(files):
            file_path = Path.joinpath(Path(root),file)
            file_hash = md5(file_path)
            if not file_hash in set_hash:
                set_hash.add(file_hash)
                with open('uniq.txt', 'a+') as f:
                    f.write(f'{file_path.resolve()} \t {file_hash} \n')
            else:
                #print(f'{file_path.resolve()} \t {file_hash} \t Not unique')
                #Duplicate file
                pass
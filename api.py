"""
Structure of local server host
Storage
    - files/
        - any files or folders used for storage
    
    - tmp/
        - any temp folders
"""
import shutil
import os
import tarfile

_REMOVE_TAR_XZ = -len(".tar.xz")

# uses tar.xz format
def encode(file_or_directory_path: str, to_path: str="./") -> None:
    shutil.make_archive(file_or_directory_path, "xztar", to_path, file_or_directory_path)


def decode(file_path: str, to_path: str="./") -> None:
    shutil.unpack_archive(filename=file_path, extract_dir=to_path, format="xztar")

def encode_for_user(file_or_directory_path: str, to_path: str) -> str:
    if os.path.isfile(file_or_directory_path):
        return file_or_directory_path
    
    shutil.make_archive(file_or_directory_path, "zip", to_path, file_or_directory_path)
    return f"{file_or_directory_path}.zip"

def get_files(directory: str) -> list[str]:
    with tarfile.open(directory, "r:xz") as fh:
        files = fh.getmembers()

    return [i.uname for i in files]

def tar_xz_path_to_normal(filename: str) -> str:
    if filename.endswith(".tar.xz"):
        return filename[:_REMOVE_TAR_XZ]
        
    return filename
def remove(path: str) -> None:
    if os.path.isfile(path):
        os.remove(path)

    else:
        shutil.rmtree(path)
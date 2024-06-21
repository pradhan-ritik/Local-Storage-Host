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

_REMOVE_TAR_XZ = -len(".tar.xz")

# uses tar.xz format
def encode(file_or_directory_path: str, to_path: str="./") -> None:
    shutil.make_archive(file_or_directory_path, "xztar", to_path, file_or_directory_path)


def decode(file_path: str, to_path: str="./") -> None:
    shutil.unpack_archive(filename=file_path, extract_dir=to_path, format="xztar")

def tar_xz_path_to_normal(filename: str) -> str:
    if filename.endswith(".tar.xz"):
        return filename[:_REMOVE_TAR_XZ]

def remove(path: str) -> None:
    if os.path.isfile(path):
        os.remove(path)

    else:
        shutil.rmtree(path)
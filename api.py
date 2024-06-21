"""
Structure of local server host
Storage
    - files/
        - any files or folders used for storage
    
    - tmp/
        - any temp folders
"""
import shutil

__all__ = [
    "encode",
    "decode"
]

# uses tar.xz format
def encode(file_or_directory_path: str, to_path: str="./") -> None:
    shutil.make_archive(file_or_directory_path, "xztar", to_path, file_or_directory_path)


def decode(file_path: str, to_path: str="./") -> None:
    shutil.unpack_archive(filename=file_path, extract_dir=to_path, format="xztar")
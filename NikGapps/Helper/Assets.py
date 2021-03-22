from .Constants import Constants
from .FileOp import FileOp
import os.path
import platform


class Assets:
    assets_folder = os.path.join(os.getcwd(), 'NikGapps', 'Assets')
    cwd = assets_folder + Constants.dir_sep
    system_name = platform.system()
    if system_name == "Windows":
        aapt_path = os.path.join(assets_folder, 'bin', system_name, 'aapt_64.exe')
        adb_path = os.path.join(assets_folder, 'bin', system_name, 'adb.exe')
    elif system_name == "Linux":
        aapt_path = "adb"
        adb_path = "aapt"
    elif system_name == "Darwin":
        aapt_path = "/Users/runner/Library/Android/sdk/build-tools/30.0.0/aapt"
        adb_path = "adb"
    else:
        aapt_path = "adb"
        adb_path = "aapt"

    @staticmethod
    def get_string_resource(file_path):
        return FileOp.read_string_file(file_path)

    @staticmethod
    def get_binary_resource(file_path):
        return FileOp.read_binary_file(file_path)

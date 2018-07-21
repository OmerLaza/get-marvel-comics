from conf import *
import os


def prep_data_dir(path=folder):
    make_data_dir(path)
    clear_data_dir(path)


def make_data_dir(path=folder):
    if not os.path.exists(path):
        os.makedirs(path)


def clear_data_dir(folder_to_del=folder):
    for the_file in os.listdir(folder_to_del):
        file_path = os.path.join(folder_to_del, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

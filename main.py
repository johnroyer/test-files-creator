# This is a sample Python script.
import os.path
import random
import string


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def run():
    print('run')

    # put file in `repository` folder
    prefix = 'repository/'
    if not os.path.exists(prefix):
        os.mkdir(prefix)

def create_folder(path):
    print('mkdir')

def create_file(path, size):
    print('create file')

def random_str(length):
    return ''.join(
        random.choice(string.ascii_letters) for i in range(length)
    )

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('creating files ...')
    run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

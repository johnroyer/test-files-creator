# This is a sample Python script.
import os.path
import random
import string

def run():
    print('run')

    # put file in `repository` folder
    prefix = 'repository/'
    if not os.path.exists(prefix):
        os.mkdir(prefix)

    # create folder
    folder_name = prefix
    depth = random.randint(1,3)
    d = 0
    while d < depth:
        folder_name += random_str(random.randint(2,6)) + '/'
        d = d + 1

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

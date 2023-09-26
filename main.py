# This is a sample Python script.
import os.path
import random
import string

def run():
    print('run')
    init()

    # create folder
    folder_name = prefix
    depth = random.randint(1,3)
    d = 0
    while d < depth:
        folder_name += random_str(random.randint(2,6)) + '/'
        d = d + 1
    create_folder(folder_name)

    # fill file in folder
    file_name = folder_name + random_str(16)
    max_file_size = 500 * 1024 * 1024 # 500MB
    file_size = random.randint(1024, max_file_size)
    with open(file_name, 'wb') as file:
        file.write(os.urandom(file_size))

def init():
    # put file in `repository` folder
    prefix = 'repository/'
    if not os.path.exists(prefix):
        os.makedirs(prefix)

def create_folder(path):
    print('creating folder: ' + path)
    os.makedirs(path)

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

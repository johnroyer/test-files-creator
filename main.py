# This is a sample Python script.
import os.path
import random
import string

def run():
    print('run')
    init()
    prefix = 'G:/test-repository/'
    repository_max_size = 500 * 1024 * 1024 * 1024 # 500GB
    repository_current_size = 0
    stop = False

    # create folder
    while stop is False:
        folder_name = prefix
        depth = random.randint(1,3)
        d = 0
        while d < depth:
            folder_name += random_str(random.randint(4,8)) + '/'
            d = d + 1
        create_folder(folder_name)

        # deside file size
        # level 1: file in Bytes
        # level 2: file in KBs
        # level 3: file in MBs
        level = random.randint(1, 3)
        if level is 1:
            min_file_size = 1
            max_file_size = 1024 - 1
            max_file_amount = 3000
        elif level is 2:
            min_file_size = 1024
            max_file_size = 1024 * 1024 - 1
            max_file_amount = 3000
        else:
            min_file_size = 1024 * 1024
            max_file_size = 300 * 1024 * 1024
            max_file_amount = 10

        # fill file in folder
        for findex in range(1, max_file_amount):
            if stop:
                print('stop at total size = ' + str(repository_current_size))
                break

            file_name = folder_name + random_str(16)

            file_size = random.randint(
                min_file_size,
                max_file_size
            )
            # make sure total size will not more than repository_max_size
            if file_size > repository_max_size - repository_current_size:
                file_size = repository_max_size - repository_current_size
                stop = True
            repository_current_size += file_size
            create_file(file_name, file_size)

def init():
    # put file in `repository` folder
    prefix = 'repository/'
    if not os.path.exists(prefix):
        os.makedirs(prefix)

def create_folder(path):
    print('creating folder: ' + path)
    os.makedirs(path)

def create_file(path, size):
    print('create file with size=' + str(size) + ' : ' + path)
    with open(path, 'wb') as file:
        file.write(os.urandom(size))

def random_str(length):
    return ''.join(
        random.choice(string.ascii_letters) for i in range(length)
    )

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

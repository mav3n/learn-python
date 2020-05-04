import random
import string
from pathlib import Path


# from com.python.utilities.random_util import random_string


def random_string(length=10, letters=string.ascii_letters):
    return ''.join(random.choice(letters) for i in range(length))


def write_random_to_file(file_path, times=1000):
    # Open a file in a write and read mode, creates a file if not exists
    txt_file = open(file_path, "w+")
    # Write something to the file
    for i in range(times):
        txt_file.write(random_string(100))
        txt_file.write(" :: %d \n" % i)
    txt_file.close()


def read_and_print_file_content(file_path):
    # Open a file for reading
    txt_file = open(file_path, "r")

    # Read and print what was written in the file
    lines = txt_file.readlines()
    for line in lines:
        print(line)


def default_file():
    home_path = Path.home()
    file_path = "%s/sample.txt" % home_path
    print(file_path)
    return file_path


def write_and_read_from_file(file_path=default_file()):
    write_random_to_file(file_path)
    read_and_print_file_content(file_path)


write_and_read_from_file()

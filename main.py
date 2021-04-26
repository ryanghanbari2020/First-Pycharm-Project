# This is a sample Python script.

import os
import argparse

def main(database:str, url_list_file:str):
    print ("We are going to work with " + database)
    print ("We are going to scan " + url_list_file)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite file name")
    parser.add_argument("-i", "--input", help="File containing urls to read")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database = database_file, url_list_file = input_file)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

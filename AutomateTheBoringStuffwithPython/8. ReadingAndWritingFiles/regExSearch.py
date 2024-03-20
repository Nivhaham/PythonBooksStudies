import re
import os


def searchUserInputInTextFilesDirectory(path: str, user_input: str = 'cool'):
    user_input = str(user_input)
    for fileName in os.listdir(path):
        if os.path.splitext(fileName)[1] == '.txt':
            with open(fileName, 'r') as file:
                for line in file.readlines():
                    if user_input in line:
                        print(line)


def main():
    user_input = input("enter a search word: \n")
    path = str(os.chdir(path=input("enter a Path:\n")))
    if path == '':
        path = os.getcwd()
    searchUserInputInTextFilesDirectory(path, user_input)


if __name__ == '__main__':
    main()

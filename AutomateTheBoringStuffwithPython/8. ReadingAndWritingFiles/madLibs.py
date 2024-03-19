import os
import re


def madLibs():
    user_adjective = input("Enter an adjective: ")
    user_noun = input("Enter a noun:")
    user_verb = input("Enter a verb:")
    user_noun2 = input("Enter a noun:")

    baseFile = open('madLibsBaseTxt.txt', 'r')
    content = baseFile.read()
    # print(content)
    newContent = content.replace('ADJECTIVE', str(user_adjective))
    newContent = newContent.replace('NOUN', str(user_noun), 1)
    newContent = newContent.replace('VERB', str(user_verb))
    newContent = newContent.replace('NOUN', str(user_noun2), 1)
    # print(newContent)
    baseFile.close()
    newFile = open('madLibsUserInputFile.txt', 'w')
    newFile.write(f'{newContent}')


if __name__ == '__main__':
    madLibs()

import re


def removingExtraSpaces(text: str):
    '''

    :param text:
    :return: The text without extraSpaces
    '''
    removingExtraSpacesRegex = re.compile(r'''\s{2,} ''', re.VERBOSE)
    res = removingExtraSpacesRegex.sub(' ', text)
    print(res)


def matchNumberWithCommaEvery3Digit(userInput: list[str] | str):
    if type(userInput) == str:
        commaPatternInNumber = r'\b(?:\d{1,3}(?:,\d{3})*|(?:\d+,)*\d+)\b'
        matches = re.findall(commaPatternInNumber, userInput)
        print(matches)

    else:
        commaPatternInNumber = r'^\d{1,3}(,\d{3})*$'
        regex = re.compile(commaPatternInNumber)
        for input_str in userInput:
            if regex.fullmatch(input_str):
                print(f"Match: {input_str}")


if __name__ == '__main__':
    text = input("Enter whatever you want with extra spaces: \n")
    removingExtraSpaces(text)
    numbers = ['100', '1,000', '10,000', '100,000', '1,000,000', '10,00,000', '10,00']
    matchNumberWithCommaEvery3Digit(numbers)

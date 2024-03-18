import re


def strongPasswordDetection(password: str):
    '''

    :param password:
    :return string that indicate if the password is strong:
    '''
    combinedPattern = r'''(?=.*\d)
                          (?=.*[A-Z])
                          (?=.*[a-z])
                          \w{8,}'''
    print(re.findall(combinedPattern, password, re.VERBOSE))
    if re.findall(combinedPattern, password, re.VERBOSE) == []:
        return "Weak Password"
    else:
        return "Strong Password"


if __name__ == '__main__':
    password = 'dfgmSDma3Aasd'
    strongPasswordDetection(password)

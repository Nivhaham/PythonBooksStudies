import re

text = 'dasda 053-543-6404 asdasdas 052-3456-4353 dsk 050-323-5343'
phoneNumRegex = re.compile(r'\d{3}-\d\d\d-\d\d\d\d')  # creating a regex object
print(phoneNumRegex.findall(text))
print(type(phoneNumRegex))
mo = phoneNumRegex.search(text)  # return a match object
print(mo.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)') # Bat prefix
batWoRegex = re.compile(r'Bat(wo)?man') # Batman and Batwoman
batWoStarRegex = re.compile(r'Bat(wo)*man')
haRegex = re.compile(r'(Ha){3}') # repeat specific numbers of time

'''
\d Any numeric digit from 0 to 9.
\D Any character that is not a numeric digit from 0 to 9.
\w Any letter, numeric digit, or the underscore character.
(Think of this as matching “word” characters.)
\W Any character that is not a letter, numeric digit, or the
underscore character.
\s Any space, tab, or newline character. (Think of this as
matching “space” characters.)
\S Any character that is not a space, tab, or newline.
'''

# greedy version vs none greedy version makes:
'''
>>> nongreedyRegex = re.compile(r'<.*?>')
>>> mo = nongreedyRegex.search('<To serve man> for dinner.>')
>>> mo.group()
'<To serve man>'
>>> greedyRegex = re.compile(r'<.*>')
>>> mo = greedyRegex.search('<To serve man> for dinner.>')
>>> mo.group()
'<To serve man> for dinner.>
'''

'''
• The ? matches zero or one of the preceding group.
• The * matches zero or more of the preceding group.
• The + matches one or more of the preceding group.
• The {n} matches exactly n of the preceding group.
• The {n,} matches n or more of the preceding group.
• The {,m} matches 0 to m of the preceding group.
• The {n,m} matches at least n and at most m of the preceding group.
• {n,m}? or *? or +? performs a nongreedy match of the preceding group.
• ^spam means the string must begin with spam.
• spam$ means the string must end with spam.
• The . matches any character, except newline characters.
• \d, \w, and \s match a digit, word, or space character, respectively.
• \D, \W, and \S match anything except a digit, word, or space character,
respectively.
• [abc] matches any character between the brackets (such as a, b, or c).
• [^abc] matches any character that isn’t between the brackets.

'''

robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())
#RoboCop
# re.I for case Insensitive

namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
#CENSORED gave the secret documents to CENSORED.

# when using multiple lines in re.compile(r''' ''') need to add re.VERBOSE()
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

'''
# Regular expression pattern to match a valid email address
pattern = r"""
    ^                   # Start of the string
    [\w\.-]+            # Username (alphanumeric, dots, and dashes)
    @                   # Literal '@' symbol
    [\w\.-]+            # Domain name (alphanumeric, dots, and dashes)
    \.                  # Literal '.' symbol
    [a-zA-Z]{2,}        # Top-level domain (e.g., .com, .org)
    $                   # End of the string
"""

# Compile the pattern with re.VERBOSE flag
regex = re.compile(pattern, re.VERBOSE)

'''
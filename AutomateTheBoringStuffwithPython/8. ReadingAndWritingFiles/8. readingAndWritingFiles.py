import os

print(os.path.join('usr', 'bin', 'spam'))
print(os.getcwd())

# os.chdir('C:\\Windows\\System32')
# os.makedirs('C:\\delicious\\walnut\\waffles')

'''
>>> os.path.abspath('.')
'C:\\Python34'
>>> os.path.abspath('.\\Scripts')
'C:\\Python34\\Scripts'
>>> os.path.isabs('.')
False
>>> os.path.isabs(os.path.abspath('.'))
True
>>> calcFilePath.split(os.path.sep)
['C:', 'Windows', 'System32', 'calc.exe']
'''

'''
Calling os.path.exists(path) will return True if the file or folder referred
to in the argument exists and will return False if it does not exist.
Calling os.path.isfile(path) will return True if the path argument exists
and is a file and will return False otherwise.
Calling os.path.isdir(path) will return True if the path argument exists
and is a folder and will return False otherwise.
'''
'''
1. Call the open() function to return a File object.
2. Call the read() or write() method on the File object.
3. Close the file by calling the close() method on the File object.
'''

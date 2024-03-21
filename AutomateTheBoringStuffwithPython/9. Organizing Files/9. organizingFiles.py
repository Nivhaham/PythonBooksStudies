import shutil, os, zipfile


'''
>>> os.chdir('C:\\')
>>> shutil.copy('C:\\spam.txt', 'C:\\delicious')
'C:\\delicious\\spam.txt'
>>> shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')
'C:\\delicious\\eggs2.txt'
>>> shutil.copytree('C:\\bacon', 'C:\\bacon_backup')  # copy the directory bacon with all of his childs
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
'C:\\eggs\\bacon.txt'
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt') # move bacon.txt and give it a new name in the eggs directory
'C:\\eggs\\new_bacon.txt' 
'''

# deleting file/folder/tree
'''
• Calling os.unlink(path) will delete the file at path.
• Calling os.rmdir(path) will delete the folder at path. This folder must be
empty of any files or folders.
• Calling shutil.rmtree(path) will remove the folder at path, and all files
and folders it contains will also be deleted.
'''

for folderName, subfolders, filenames in os.walk(r'C:\Users\niv_d\PycharmProjects\PythonBooks'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
    print('')

'''
>>> os.chdir('C:\\') # move to the folder with example.zip
>>> exampleZip = zipfile.ZipFile('example.zip')  
>>> exampleZip.namelist() # returning a list of all the files that inside the zip file
['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
>>> spamInfo = exampleZip.getinfo('spam.txt')
>>> spamInfo.file_size
13908
>>> spamInfo.compress_size
3828
>>> 'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo
.compress_size, 2))
'Compressed file is 3.63x smaller!'
>>> exampleZip.close()
'''

# Extracting from Zip file
'''
>>> exampleZip.extractall()
>>> exampleZip.extract('spam.txt')
'C:\\spam.txt'
>>> exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
'C:\\some\\new\\folders\\spam.txt'
>>> exampleZip.close()
'''

# write to Zip file
'''
>>> import zipfile
>>> newZip = zipfile.ZipFile('new.zip', 'w')
>>> newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
>>> newZip.close()
'''
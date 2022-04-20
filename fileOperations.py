#Basic file operations to be used by other projects
#version 1.1

import os.path


def checkIfFileExists(myFile):
    return os.path.exists(myFile)

def readLinesFromFile(myfile):

    fileContent = []

    try:
        with open(myfile, errors='ignore') as f:
            # do something with f
            fileContent = f.readlines()
    except OSError as e:
        print('Exception: '+ e)
        
    return fileContent

def writeContentsToFile(fileContent, targetFile, endOfLineCharacters='\n'):
    try:
        with open(targetFile, "w") as text_file:
            output = endOfLineCharacters.join(fileContent)
            text_file.write(output)
            pass
    except OSError as e:
        print('Exception: '+ e)

def writeStringToFile(fullPathToFile, contentToWrite , fileEncoding='utf-8'):
    try:
        with open(fullPathToFile, 'w', encoding=fileEncoding) as newFile:
            newFile.write(contentToWrite)
    except IOError as e:
        print(e)

def stripLines(fileContent):
    modifiedFileContent = []
    for line in fileContent:
        modifiedFileContent.append(line.strip('\n'))

    return modifiedFileContent

def stripLinesFromWhitespace(fileContent):
    modifiedFileContent = []
    for line in fileContent:
        modifiedFileContent.append(line.strip())

    return modifiedFileContent
    
    
def getFileDiff(file1, file2):
    import subprocess
    from shutil import copyfile

    return subprocess.check_output(["diff", file1, file2]).decode('utf-8')
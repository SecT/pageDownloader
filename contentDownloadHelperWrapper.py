# from urllib.request import urlretrieve
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from shutil import copyfileobj

from .contentDownloadHelper import getPageContents as generalGetPageContents
from .contentDownloadHelper import saveImg as generalSaveImg

class ContentDownloadHelperWrapper:
    def __init__(self):
        pass

    def getPageContents(url, charset):

        return generalGetPageContents(url, charset)

    def saveContentToFile(filename, content, targetDir, format='htm', fileEncoding='utf-8'):

        filename = filename.replace(':', '-')
        filename = filename.replace('<', '_')
        filename = filename.replace('>', '_')

        try:
            with open(targetDir + filename + '.' + format, 'w', encoding=fileEncoding) as newFile:
                newFile.write(content)
        except IOError as e:
            print(e)

    def saveImg(url, filename, targetDir):
        generalSaveImg(url, filename, targetDir)

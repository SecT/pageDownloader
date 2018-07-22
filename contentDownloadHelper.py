from urllib.request import urlretrieve


class ContentDownloadHelper:
    def __init__(self):
        pass

    def saveContentToFile( filename, content, targetDir, format='htm', fileEncoding='utf-8'):

        filename = filename.replace(':','-')
        filename = filename.replace('<', '_')
        filename = filename.replace('>', '_')

        newFile = open(targetDir+filename+'.'+format, 'w', encoding=fileEncoding)
        newFile.write(content)
        newFile.close()

    def saveImg( url, filename, targetDir):
        urlretrieve(url, targetDir+filename)


from urllib.request import urlretrieve


class ContentDownloadHelper:
    def __init__(self):
        pass

    def saveContentToFile( filename, content, format='htm', fileEncoding='utf-8'):
        newFile = open(filename+'.'+format, 'w', encoding=fileEncoding)
        newFile.write(content)
        newFile.close()

    def saveImg( url, filename):
        urlretrieve(url, filename)


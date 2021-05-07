#from urllib.request import urlretrieve
from urllib.request import Request, urlopen
from shutil import copyfileobj

class ContentDownloadHelper:
    def __init__(self):
        pass

    def getPageContents(url, charset):

        req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req)
        return page.read().decode(charset, 'ignore')

    def saveContentToFile( filename, content, targetDir, format='htm', fileEncoding='utf-8'):

        filename = filename.replace(':','-')
        filename = filename.replace('<', '_')
        filename = filename.replace('>', '_')

        try:
            with open(targetDir+filename+'.'+format, 'w', encoding=fileEncoding) as newFile:
                newFile.write(content)
        except IOError as e:
            print(e)

    def saveImg( url, filename, targetDir):
        #urlretrieve(url, targetDir+filename)  #urlretrieve is deprecated, see python docs

        print('saveImg: '+url)
        req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

        with urlopen(req) as in_stream, open(targetDir+filename, 'wb') as out_file:
            copyfileobj(in_stream, out_file)


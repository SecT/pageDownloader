import urllib.request

from time import sleep

class LinearUrlDownloader:

    def __init__(self, url, base, pageDownloadDelay=0, limit=-1):
        self.currentPageContent = ''

        self.baseUrl = url
        self.currentUrl = self.baseUrl

        self.base = base

        self.pageDownloadDelay = pageDownloadDelay  # [s] in order to avoid overloading the server

        self.limit = limit

        self.charset = 'utf-8' #default

        self.currentNumberOfPageDownloaded = 0

        self.targetDir = ''

    def setCharset(self, charset):
        self.charset = charset

    def setTargetDir(self, targetDir):
        self.targetDir = targetDir

    def downloadPage(self):

        for i in range(self.limit):

            pageId = self.generatePageId(self.base + i)

            nextUrl = self.baseUrl + str(pageId)

            print(nextUrl)

            currentPageContent = self.getPageContents(nextUrl)
            self.processPage(currentPageContent)

            self.currentNumberOfPageDownloaded+=1

        self.postProcess()

        return

    #to override
    def generatePageId(self, i):
        pass


    def getPageContents(self, url):
        page = urllib.request.urlopen(url)
        return page.read().decode(self.charset)

    #to override
    def processPage(self, pageContent):
        return

    #to override
    def postProcess(self):
        return
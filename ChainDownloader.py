#use with python3

#HOW TO USE
#Import the ChainPageDownloader class
#Create a new class, inheriting from ChainPageDownloader
#Define a constructor. The constructor should call the ChainPageDownloader constructor
#Override methods: generateNextPageUrl(), processPage(), postProcess()
#Create an instance of the new class
#Call downloadPage()

import urllib.request

from time import sleep


class ChainDownloader:

    def __init__(self, url, pageDownloadDelay=0, limit=-1):
        self.currentPageContent = ''

        self.root = url
        self.currentUrl = self.root

        self.pageDownloadDelay = pageDownloadDelay  # [s] in order to avoid overloading the server

        self.limit = limit

        self.charset = 'utf-8' #default

    def setCharset(self, charset):
        self.charset = charset

    #download the whole chain-type website
    def downloadPage(self):

        self.currentPageContent = self.getCurrentPageContents()

        self.processPage()


        nextPageUrl = self.getNextPageUrl()


        while nextPageUrl != False:
            print(nextPageUrl)
            self.currentUrl = nextPageUrl
            self.currentPageContent = self.getCurrentPageContents()

            self.processPage()

            nextPageUrl = self.getNextPageUrl()

            sleep(self.pageDownloadDelay)

        self.postProcess()

        return

    def getNextPageUrl(self):
        newUrl = self.generateNextPageUrl()

        if newUrl != '':
            return newUrl
        return False

    #to override
    def generateNextPageUrl(self):
        pass

    def getCurrentPageContents(self):
        page = urllib.request.urlopen(self.currentUrl)
        return page.read().decode(self.charset)

    #to override
    def processPage(self):
        return

    #to override
    def postProcess(self):
        return
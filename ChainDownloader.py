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

from pageDownloader.regexHelper import RegexHelper
from pageDownloader.contentDownloadHelper import ContentDownloadHelper


class ChainDownloader:

    def __init__(self, url, prefix, urlRegexPatterns, contentRegexPatterns, pageDownloadDelay=0, limit=-1):
        self.currentPageContent = ''

        self.root = url
        self.currentUrl = self.root

        self.prefix = prefix

        self.urlRegexPatterns = urlRegexPatterns

        self.contentRegexPatterns = contentRegexPatterns

        self.pageDownloadDelay = pageDownloadDelay  # [s] in order to avoid overloading the server

        self.limit = limit

        self.pageNumber = 0

        self.charset = 'utf-8' #default

        self.targetDir = ''

        self.base = 0

        self.data = ''

        self.processMode = ''

    def setCharset(self, charset):
        self.charset = charset

    def setTargetDir(self, targetDir):
        self.targetDir = targetDir

    def setProcessMode(self, mode):
        self.processMode = mode

    #download the whole chain-type website
    def downloadPage(self):

        #self.currentPageContent = self.getCurrentPageContents()
        self.currentPageContent = ContentDownloadHelper.getPageContents(self.currentUrl, self.charset)

        self.processPage()

        self.pageNumber+=1

        nextPageUrl = self.getNextPageUrl()


        while nextPageUrl != False:
            print(nextPageUrl)
            self.currentUrl = nextPageUrl
            self.currentPageContent = ContentDownloadHelper.getPageContents(self.currentUrl, self.charset)

            self.processPage()

            nextPageUrl = self.getNextPageUrl()

            self.pageNumber+=1

            if self.limit > 0 and self.pageNumber >= self.limit:
                break

            sleep(self.pageDownloadDelay)

        self.postProcess()

        return

    def getNextPageUrl(self):
        newUrl = self.generateNextPageUrl()

        if newUrl != '':
            return newUrl
        return False


    def generateNextPageUrl(self):

        haystack = self.currentPageContent

        for pattern in self.urlRegexPatterns:
            url = RegexHelper.generateSingleMatch(pattern, haystack)

            if url != False:
                haystack = url
            else:
                print("Finished")
                return False

        url = haystack

        url = url.replace('&amp;', '&')

        url = self.prefix + url

        return url

    #to override
    def processPage(self):

        self.processPagePlaceholder1()

        newContent = self.currentPageContent

        for pattern in self.contentRegexPatterns:
            newContent = RegexHelper.generateSingleMatch(pattern, newContent)

        if self.processMode == 'story':
            if newContent != False:
                #self.data +=  "<br><br><br>"

                #append chapter to string
                self.data +=  newContent

                #self.chapter += 1
        elif self.processMode == 'image':
            pass


        self.processPagePlaceholder2()

        return


    #to override
    def postProcess(self):
        if self.processMode == 'story':
            ContentDownloadHelper.saveContentToFile('story', self.data, self.targetDir, 'htm')
        return

    #to override
    def processPagePlaceholder1(self):
        pass

    #to override
    def processPagePlaceholder2(self):
        pass
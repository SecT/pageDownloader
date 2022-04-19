# use with python3

# HOW TO USE
# Import the ChainPageDownloader class
# Create a new class, inheriting from ChainPageDownloader
# Define a constructor. The constructor should call the ChainPageDownloader constructor
# Override methods: generateNextPageUrl(), processPage(), postProcess()
# Create an instance of the new class
# Call downloadPage()

import urllib.request
from http.client import InvalidURL

from time import sleep

from pageDownloader.regexHelper import RegexHelper
from pageDownloader.contentDownloadHelperWrapper import ContentDownloadHelperWrapper


class ChainDownloader:

    def __init__(self, url, prefix, urlRegexPatterns, contentRegexPatterns, pageDownloadDelay=0, limit=-1,
                 contentPrefix=''):
        self.currentPageContent = ''

        self.root = url
        self.currentUrl = self.root

        self.prefix = prefix
        self.contentPrefix = contentPrefix

        self.urlRegexPatterns = urlRegexPatterns

        self.contentRegexPatterns = contentRegexPatterns

        self.pageDownloadDelay = pageDownloadDelay  # [s] in order to avoid overloading the server

        self.limit = limit

        self.currentNumberOfPageDownloaded = 0

        self.charset = 'utf-8'  # default

        self.targetDir = ''

        self.base = 0

        self.data = ''

        self.processMode = ''

        self.problematicUrlsList = []

    def setCharset(self, charset):
        self.charset = charset

    def setTargetDir(self, targetDir):
        self.targetDir = targetDir

    def setProcessMode(self, mode):
        self.processMode = mode

    # download the whole chain-type website
    def downloadPage(self):

        if self.processMode == '':
            print('Error. Process mode is not set. Aborting')
            return

        nextPageUrl = self.currentUrl

        # while nextPageUrl != False:
        while not self.isStop(0, nextPageUrl):
            print(nextPageUrl)
            self.currentUrl = nextPageUrl
            self.currentPageContent = ContentDownloadHelperWrapper.getPageContents(self.currentUrl, self.charset)

            self.processPage()

            nextPageUrl = self.getNextPageUrl()

            self.currentNumberOfPageDownloaded += 1

            if self.limit > 0 and self.currentNumberOfPageDownloaded > self.limit:
                break

            sleep(self.pageDownloadDelay)

        self.postProcess()

        if len(self.problematicUrlsList) > 0:
            print("Some pages could not have been downloaded:")

            for page in self.problematicUrlsList:
                print(page)

        return

    def isStop(self, currentId, nextPageUrl):
        if not nextPageUrl:
            return True

    def getNextPageUrl(self, currentId=0):
        newUrl = self.generateNextPageUrl()

        if newUrl != '':
            return newUrl
        return False

    def generateNextPageUrl(self, currentId=0):

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

    # to override
    def processPage(self):

        self.processPagePlaceholder1()

        newContent = self.currentPageContent

        for pattern in self.contentRegexPatterns:
            newContent = RegexHelper.generateSingleMatch(pattern, newContent)

        if self.processMode == 'story':
            if newContent != False:
                # self.data +=  "<br><br><br>"

                # append chapter to string
                self.data += newContent

                # self.chapter += 1Ł
        elif self.processMode == 'image':
            if newContent != False:
                fileFormat = self.getFileFormat(newContent)

                newContent = self.contentPrefix + newContent

                try:
                    ContentDownloadHelperWrapper.saveImg(newContent, self.getImageFileName(fileFormat), self.targetDir)
                except InvalidURL:
                    self.problematicUrlsList.append(imgAddress)

        self.processPagePlaceholder2()

        return True

    # to override
    def getFileFormat(self, content):
        return content[-3:]

    def getImageFileName(self, fileFormat):
        return str(self.currentNumberOfPageDownloaded).zfill(4) + "." + fileFormat

    # to override
    def postProcess(self):
        if self.processMode == 'story':
            ContentDownloadHelperWrapper.saveContentToFile('story', self.data, self.targetDir, 'htm')
        return True

    # to override
    def processPagePlaceholder1(self):
        pass

    # to override
    def processPagePlaceholder2(self):
        pass

import urllib.request
from http.client import InvalidURL

from time import sleep
from pageDownloader.regexHelper import RegexHelper
from pageDownloader.contentDownloadHelper import ContentDownloadHelper


class LinearUrlDownloader:

    def __init__(self, url, base, prefix, urlRegexPatterns, pageDownloadDelay=0, limit=-1):
        self.currentPageContent = ''

        self.baseUrl = url
        self.currentUrl = self.baseUrl

        self.base = base

        self.prefix = prefix

        self.urlRegexPatterns = urlRegexPatterns

        self.pageDownloadDelay = pageDownloadDelay  # [s] in order to avoid overloading the server

        self.limit = limit

        self.charset = 'utf-8'  # default

        self.currentNumberOfPageDownloaded = 0

        self.targetDir = ''

        self.problematicUrlsList = []

    def setCharset(self, charset):
        self.charset = charset

    def setTargetDir(self, targetDir):
        self.targetDir = targetDir

    def downloadPage(self):

        # for i in range(self.limit):

        currentId = 0

        while not self.isStop(currentId, ''):
            nextUrl = self.getNextPageUrl(currentId)

            print(nextUrl)

            currentPageContent = ContentDownloadHelper.getPageContents(nextUrl, self.charset)

            if not self.skip(currentPageContent):
                self.processPage(currentPageContent)

                self.currentNumberOfPageDownloaded += 1

                sleep(self.pageDownloadDelay)

            currentId += 1

        self.postProcess()

        if len(self.problematicUrlsList) > 0:
            print("Some pages could not have been downloaded:")

            for page in self.problematicUrlsList:
                print(page)

        return True

    def isStop(self, currentId, nextPageUrl):
        if currentId >= self.limit:
            return True

    def getNextPageUrl(self, currentId=0):

        nextUrl = self.generateNextPageUrl(currentId)

        if nextUrl != '':
            return nextUrl

        return nextUrl

    def generateNextPageUrl(self, currentId=0):
        pageId = self.generatePageId(self.base + currentId)

        nextUrl = self.baseUrl + str(pageId)

        return nextUrl

    # to override if default is not suitable
    def generatePageId(self, i):
        return i

    # to override if default is not suitable
    def processPage(self, pageContent):

        imgAddress = pageContent

        for pattern in self.urlRegexPatterns:

            if imgAddress != False:
                imgAddress = RegexHelper.generateSingleMatch(pattern, imgAddress)
            else:
                print("Regex error for page number: " + str(self.currentNumberOfPageDownloaded + self.base))
                return

        # print('pattern: '+pattern)
        # print('imgAddress: '+imgAddress)
        if imgAddress != False:

            stripNumber = str(self.currentNumberOfPageDownloaded + self.base).zfill(4)

            fileFormat = self.getFormatName(imgAddress)

            imgAddress = self.prefix + imgAddress

            print('imgAddress: ' + imgAddress)

            try:
                ContentDownloadHelper.saveImg(imgAddress, stripNumber + "." + fileFormat, self.targetDir)
            except InvalidURL:
                self.problematicUrlsList.append(imgAddress)

        return True

    # to override if default is not suitable
    def skip(self, pageContent):
        return False

    # to override
    def postProcess(self):
        return

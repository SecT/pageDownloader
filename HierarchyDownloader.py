import urllib.request

from time import sleep

from pageDownloader.regexHelper import RegexHelper

class HierarchyDownloader:

    def __init__(self, url,prefix, urlRegexPatterns, pageDownloadDelay=0, limit=-1):
        self.currentPageContent = ''

        self.root = url
        self.currentUrl = self.root

        self.prefix = prefix

        self.urlRegexPatterns = urlRegexPatterns

        self.pageDownloadDelay = pageDownloadDelay  # [s] in order to avoid overloading the server

        self.limit = limit

        self.charset = 'utf-8' #default

        self.currentNumberOfPageDownloaded = 0

        self.targetDir = ''

    def setCharset(self, charset):
        self.charset = charset

    def setFormat(self, fileFormat):
        self.format = fileFormat

    def setTargetDir(self, targetDir):
        self.targetDir = targetDir

    #download the whole hierarchy-type website
    #TEMP: download one level only
    def downloadPage(self):

        currentPageContent = self.getPageContents(self.root)

        self.processPage(currentPageContent)


        nextLevelUrls = self.getNextLevelUrls(currentPageContent)

        for url in nextLevelUrls:
            print(url)

            currentPageContent = self.getPageContents(url)

            self.processPage(currentPageContent)

            sleep(self.pageDownloadDelay)

            self.currentNumberOfPageDownloaded += 1

            if self.currentNumberOfPageDownloaded == self.limit:
                print("Reached the set page limit. Stopping download...")
                break

        self.postProcess()

        return

    def getNextLevelUrls(self, pageContent):

        nextLevelUrls = self.generateNextLevelUrls(pageContent)

        if len(nextLevelUrls) > 0:
            return nextLevelUrls

        return False


    def generateNextLevelUrls(self, pageContent):
        rawUrls = RegexHelper.generateMultipleMatches(self.urlRegexPatterns[0],pageContent)

        #TODO: temporarily only works for urlRegexPatterns of size 1

        urls = list()

        for url in rawUrls:

            urls.append(self.prefix+url)

        return urls

    def getPageContents(self, url):
        page = urllib.request.urlopen(url)
        return page.read().decode(self.charset)

    #to override
    def processPage(self, pageContent):
        return

    #to override
    def postProcess(self):
        return
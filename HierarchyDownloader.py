import urllib.request

from time import sleep

class HierarchyDownloader:

    def __init__(self, url, pageDownloadDelay=0, limit=-1):
        self.currentPageContent = ''

        self.root = url
        self.currentUrl = self.root

        self.pageDownloadDelay = pageDownloadDelay  # [s] in order to avoid overloading the server

        self.limit = limit

        self.charset = 'utf-8' #default

        self.currentNumberOfPageDownloaded = 0

    def setCharset(self, charset):
        self.charset = charset

    def setFormat(self, fileFormat):
        self.format = fileFormat

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

    #to override
    def generateNextLevelUrls(self, pageContent):
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
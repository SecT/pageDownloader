from os import remove, listdir
from unittest import TestCase
from os import listdir

class ConcreteHierarchyDownloaderTest:
    def clean(self):
        for key in self.testData:
            try:
                remove(key)
            except OSError:
                pass

        for name in listdir("."):
            if name.endswith(self.downloader.fileFormat):
                try:
                    remove(name)
                except OSError:
                    pass

    def setTestData(self, testData):
        self.testData = testData #dictionary of [fileName, numberOfChars]

    def setNumberOfFiles(self, numberOfFiles):
        self.numberOfFiles = numberOfFiles

    def test_downloadPage(self):
        self.downloader.downloadPage()

        #check number of files of given format
        #assuming no other files of the format in the test dir
        count = 0
        for name in listdir("."):
            if name.endswith(self.downloader.fileFormat):
                count+=1
        TestCase('__init__').assertEqual(count, self.numberOfFiles)
        ##

        #compare number of chars
        for key, val in self.testData.items():
            fileToRead = open(key, 'r')
            contents = fileToRead.read()
            fileToRead.close()

            TestCase('__init__').assertEqual(len(contents), val)  #we do not have an instance of TestCase
            ###
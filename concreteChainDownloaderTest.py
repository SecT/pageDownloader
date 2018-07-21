from os import remove
from unittest import TestCase

class ConcreteChainDownloaderTest():
    def clean(self):
        try:
            remove(self.fileName)
        except OSError:
            pass

    def setFileName(self, fileName):
        self.fileName = fileName

    def setNumberOfCharacters(self, numberOfChars):
        self.numberOfChars = numberOfChars

    def test_downloadPage(self):
        self.downloader.downloadPage()

        #compare number of chars

        fileToRead = open(self.fileName, 'r')
        contents = fileToRead.read()
        fileToRead.close()

        TestCase('__init__').assertEqual(len(contents), self.numberOfChars)  #we do not have an instance of TestCase
        ###
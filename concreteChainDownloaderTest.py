from os import remove, mkdir
from unittest import TestCase

import datetime

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

    def setTargetDir(self, targetDir):
        self.targetDir = targetDir

    def createTestDir(self, dirNamePrefix):
        now = datetime.datetime.now()

        datetimeForDirName = str(now.year).zfill(4)+str(now.month).zfill(2)+str(now.day).zfill(2)+'_'+str(now.hour).zfill(2)+str(now.minute).zfill(2)
        targetDir = dirNamePrefix+'_'+ datetimeForDirName

        mkdir(targetDir)

        self.setTargetDir(targetDir+"/")

    def test_downloadPage(self):
        self.downloader.downloadPage()

        #compare number of chars

        fileToRead = open(self.targetDir+self.fileName, 'r')
        contents = fileToRead.read()
        fileToRead.close()

        TestCase('__init__').assertEqual(len(contents), self.numberOfChars)  #we do not have an instance of TestCase
        ###
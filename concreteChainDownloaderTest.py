from os import remove, mkdir
from unittest import TestCase

from os.path import isfile

import datetime

class ConcreteChainDownloaderTest():
    def clean(self):
        if self.testMode == 'story':
            try:
                remove(self.fileName)
            except OSError:
                pass
        elif self.testMode == 'image':
            for i in range(self.downloader.base, self.downloader.limit+1):
                try:
                    remove(str(i).zfill(4)+self.format)
                except OSError:
                    pass

    def setFileFormat(self, fileFormat):
        self.format = fileFormat

    def setFileName(self, fileName):
        self.fileName = fileName

    def setNumberOfCharacters(self, numberOfChars):
        self.numberOfChars = numberOfChars

    def setTargetDir(self, targetDir):
        self.targetDir = targetDir

    def setTestMode(self, testMode):
        self.testMode = testMode

    def createTestDir(self, dirNamePrefix):
        now = datetime.datetime.now()

        datetimeForDirName = str(now.year).zfill(4)+str(now.month).zfill(2)+str(now.day).zfill(2)+'_'+str(now.hour).zfill(2)+str(now.minute).zfill(2)
        targetDir = dirNamePrefix+'_'+ datetimeForDirName

        mkdir(targetDir)

        self.setTargetDir(targetDir+"/")

    def test_downloadPage(self):
        self.downloader.downloadPage()

        if self.testMode == 'story':

            #compare number of chars

            fileToRead = open(self.targetDir+self.fileName, 'r')
            contents = fileToRead.read()
            fileToRead.close()

            TestCase('__init__').assertEqual(len(contents), self.numberOfChars)  #we do not have an instance of TestCase
            ###

        elif self.testMode == 'image':
            self.downloader.downloadPage()

            for i in range(self.downloader.base, self.downloader.limit+1):
                print('Checking if file exists: '+self.targetDir+str(i).zfill(4)+self.format)
                self.assertTrue(isfile(self.targetDir+str(i).zfill(4)+self.format))

            print('Checking if file '+self.targetDir+str(i+1).zfill(4)+self.format+' exists. It should not exist.')
            self.assertFalse(isfile(self.targetDir+str(i+1).zfill(4)+self.format)) #no more images have been downloaded then limit

        else:
            pass
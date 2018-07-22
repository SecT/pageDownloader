from os import remove, listdir
from unittest import TestCase
from os import listdir,mkdir

import datetime

class ConcreteHierarchyDownloaderTest:
    def clean(self):
        for key in self.testData:
            try:
                remove(key)
            except OSError:
                pass

            try:
                for name in listdir(self.downloader.targetDir):
                    if name.endswith(self.downloader.fileFormat):

                        remove(name)

            except OSError:
                pass

    def createTestDir(self, dirNamePrefix):
        now = datetime.datetime.now()

        datetimeForDirName = str(now.year).zfill(4)+str(now.month).zfill(2)+str(now.day).zfill(2)+'_'+str(now.hour).zfill(2)+str(now.minute).zfill(2)
        targetDir = dirNamePrefix+'_'+ datetimeForDirName

        mkdir(targetDir)

        self.setTargetDir(targetDir+"/")


    def setTestData(self, testData):
        self.testData = testData #dictionary of [fileName, numberOfChars]

    def setNumberOfFiles(self, numberOfFiles):
        self.numberOfFiles = numberOfFiles

    def setTargetDir(self, targetDir):
        self.targetDir = targetDir

    def test_downloadPage(self):
        self.downloader.downloadPage()

        #check number of files of given format
        #assuming no other files of the format in the test dir
        count = 0
        for name in listdir(self.targetDir):
            if name.endswith(self.downloader.fileFormat):
                count+=1
        TestCase('__init__').assertEqual(count, self.numberOfFiles)
        ##

        #compare number of chars
        for key, val in self.testData.items():
            fileToRead = open(self.targetDir+key, 'r')
            contents = fileToRead.read()
            fileToRead.close()

            TestCase('__init__').assertEqual(len(contents), val)  #we do not have an instance of TestCase
            ###
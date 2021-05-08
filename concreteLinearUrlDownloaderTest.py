from unittest import TestCase
from unittest import main

import datetime

from os.path import isfile
from os import remove, mkdir


class ConcreteLinearUrlDownloaderTest():

    def setFileFormat(self, fileFormat):
        self.format = fileFormat

    def setTargetDir(self, targetDir):
        self.targetDir = targetDir

    def createTestDir(self, dirNamePrefix):
        now = datetime.datetime.now()

        datetimeForDirName = str(now.year).zfill(4)+str(now.month).zfill(2)+str(now.day).zfill(2)+'_'+str(now.hour).zfill(2)+str(now.minute).zfill(2)+'_'+str(now.second).zfill(2)
        targetDir = dirNamePrefix+'_'+ datetimeForDirName

        mkdir(targetDir)

        self.setTargetDir(targetDir+"/")

    def clean(self):
        for i in range(self.downloader.base, self.downloader.limit+1):
            try:
                remove(str(i).zfill(4)+self.format)
            except OSError:
                pass

    def test_downloadPage(self):

        self.downloader.downloadPage()

        for i in range(self.downloader.base, self.downloader.limit+self.downloader.base):
            print('Checking if file exists: '+self.targetDir+str(i).zfill(4)+self.format)
            self.assertTrue(isfile(self.targetDir+str(i).zfill(4)+self.format))

        print('Checking if file '+self.targetDir+str(i+1).zfill(4)+self.format+' exists. It should not exist.')
        self.assertFalse(isfile(self.targetDir+str(i+1).zfill(4)+self.format)) #no more images have been downloaded then limit

        pass
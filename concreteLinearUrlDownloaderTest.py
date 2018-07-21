from unittest import TestCase
from unittest import main

from os.path import isfile
from os import remove


class ConcreteLinearUrlDownloaderTest():

    def setFileFormat(self, fileFormat):
        self.format = fileFormat

    def clean(self):
        for i in range(self.downloader.base, self.downloader.limit+1):
            remove(str(i).zfill(4)+self.format)

    def test_downloadPage(self):

        self.downloader.downloadPage()

        for i in range(self.downloader.base, self.downloader.limit+1):
            print('Checking if file exists: '+str(i).zfill(4)+self.format)
            self.assertTrue(isfile(str(i).zfill(4)+self.format))

        print('Checking if file '+str(i+1).zfill(4)+self.format+' exists. It should not exist.')
        self.assertFalse(isfile(str(i+1).zfill(4)+self.format)) #no more images have been downloaded then limit

        pass
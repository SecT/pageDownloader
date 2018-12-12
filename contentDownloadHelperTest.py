import unittest

from os.path import join
from os import remove

from contentDownloadHelper import ContentDownloadHelper

class ContentDownloadHelperTest(unittest.TestCase):

    def test_saveContentToFile(self):
        filename = 'test_saveContentToFile_00'
        content = '0123456789abcążźćęółńś'
        path = ''
        format = 'txt'
        ContentDownloadHelper.saveContentToFile(filename, content,path , format)

        try:
            with open(join(path, filename+'.'+format)) as f:
                self.assertEqual(f.read(), content)
        except IOError as e:
            print(e)

    def tearDown(self):

        remove('test_saveContentToFile_00.txt')

if __name__ == '__main__':
    unittest.main()


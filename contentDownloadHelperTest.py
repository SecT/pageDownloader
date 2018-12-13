import unittest

from os.path import join
from os import remove
import filecmp

from contentDownloadHelper import ContentDownloadHelper

class ContentDownloadHelperTest(unittest.TestCase):

	def test_getPageContents(self):
		
		url = 'https://google.com'
		charset = 'utf-8'
		
		content = ContentDownloadHelper.getPageContents(url, charset)
		
		self.assertTrue(len(content) > 100)

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

	def test_saveImg(self):

		ContentDownloadHelper.saveImg('https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png', 'test_saveImg_00.png', '')

		filecmp.cmp('test_saveImg_00.png', 'test_saveImg_00_forComparison.png')

	@classmethod
	def tearDownClass(cls):
		remove('test_saveContentToFile_00.txt')
		remove('test_saveImg_00.png')

if __name__ == '__main__':
	unittest.main()


from unittest import TestCase
from unittest import main
from unittest.mock import patch

from ChainDownloader import ChainDownloader

class mockedMethod:

    counter = 0

    def mock_generateNextPageUrl():
        mockedMethod.counter+=1
        if mockedMethod.counter < ChainDownloaderTest.maxNumberOfPages:
            return 'page_'+str(mockedMethod.counter)
        return ''

class ChainDownloaderTest(TestCase):

    maxNumberOfPages = 5

    #@patch('ChainDownloader.ChainDownloader')
    @patch('ChainDownloader.ChainDownloader.getCurrentPageContents')
    @patch('ChainDownloader.ChainDownloader.generateNextPageUrl', side_effect=mockedMethod.mock_generateNextPageUrl)
    @patch('ChainDownloader.ChainDownloader.processPage')
    def test_downloadPage(self, MockGetCurrentPageContents, MockGenerateNextPageUrl, MockProcessPage ):
        downloader = ChainDownloader("MockAddress.com")
        MockGetCurrentPageContents.return_value = "<html><body><next link='page_0'></next></body></html>"

        downloader.downloadPage()

        assert MockGenerateNextPageUrl.call_count == ChainDownloaderTest.maxNumberOfPages
        assert MockProcessPage.call_count == ChainDownloaderTest.maxNumberOfPages

if __name__ == '__main__':
    main()
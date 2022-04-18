# pageDownloader
A generic web-scraper written in Python.


How to use:
Create an instance of one of the pageDownloader classes (ChainDownloader, LinearUrlDownloader , HierarchyDownloader).
Provide the regex expressions needed to obtain the content you want to download from a website, and an expression to obtain the link to the next page.
Configure the type of content you want to download (text, image).
Run downloadPage() on the pageDownloader instance.


Main pageDownloader classes:

- ChainDownloader - used for websites like webcomics, where you enter the page, see the content, and click "Next" to get to the next piece of content.

Provide the regex to get the content on the current page, and a regex to obtain the link to the next page.


- LinearUrlDownloader - similar to ChainDownloader. Used for websites like webcomics, where you enter the page, see the content, and click "Next" to get to the next piece of content.

The difference to ChainDownloader is that you do not need to provide the regex to obtain the link to the next page, since the url can be deduced otherwise (like "comic.com/page/1", "comic.com/page/2", and so on )

- HierarchyDownloader - used for websites with a tree-like structure. First, the base url is visited, where you obtain a list of urls to content. Then each of these urls is visited and the content can be downloaded.

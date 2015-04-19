import wget
import re
import sys
import urllib
import urlparse
from BeautifulSoup import BeautifulSoup

class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'

def process(url):
    myopener = MyOpener()
    #page = urllib.urlopen(url)
    page = myopener.open(url)

    text = page.read()
    page.close()

    soup = BeautifulSoup(text)

    for tag in soup.findAll('a', href=True):
        tag['href'] = urlparse.urljoin(url, tag['href'])
        if 'pdf' in tag['href']:
            print tag['href']
            wget.download(tag['href'])
# process(url)

def main():
    if len(sys.argv) == 1:
        print "Jabba's Link Extractor v0.1"
        print "Usage: %s URL [URL]..." % sys.argv[0]
        sys.exit(-1)
    # else, if at least one parameter was passed
    for url in sys.argv[1:]:
        process(url)

# main()

if __name__ == "__main__":
    main()
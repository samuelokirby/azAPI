from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep

# Returns raw HTML string.
def rawFromUrl(url):

    html = urlopen(url).read()
    raw = BeautifulSoup(html)

    return raw

# Returns an array of strings of separate lyrics from an artist's page.
# Because this is an unofficial API, oftentimes azlyrics.com will
# automatically throttle your connection if you start downloading
# too many songs at a time. Timeout is the pause between lyric
# downloads. If you don't want any pauses, put it to 0.
def lyricsFromArtist(url, timeout):

    links = []
    raw = rawFromUrl(url)
    count = 0
    for link in raw.findAll(href=True):
        if(count >= 34):
            link = str(link)
            link = link[9:]
            link = link.split("\"")
            link = link[0]
            link = link.replace("..", "http://www.azlyrics.com")
            if(link[:2] == "//" or link.endswith(".php")):
                continue
            else:
                links.append(lyricsFromUrl(link))
                sleep(timeout)
                print(link)

        count = count + 1
        #links.append(lyricsFromUrl(link.get('href')))

    # textfile = open('lyrics.txt', 'w')
    # fullString = ''.join(links)
    # textfile.write(fullString)
    print(links)

# Returns a single string of lyrics from a single page.
def lyricsFromUrl(url):

    raw = rawFromUrl(url).getText()
    raw = raw.split("\n",133)[133]
    raw = raw.split("\n\n\n\n")

    return(raw[0])

#print(lyricsFromUrl("https://www.azlyrics.com/lyrics/eminem/rapgod.html"))

lyricsFromArtist("https://www.azlyrics.com/e/eminem.html", 10)
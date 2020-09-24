import re #REGEX library
import urllib.request #Open URLs
#import markovify #Generate a Markov chain

originalLyrics = open('lyricslyricslyricslyrics.txt', 'w')
url = "https://www.azlyrics.com/c/coldplay.html"
artistHtml = urllib.request.urlopen(url)
artistHtmlStr = str(artistHtml.read())
links = re.findall('href="([^"]+)', artistHtmlStr)

songLinks = []
for x in links:
 if "lyrics/coldplay" in x:
  x = x.replace("..", "")
  x = "https://www.azlyrics.com/" + x
  songLinks.append(x)

for x in songLinks:
 songHtml = urllib.request.urlopen(x)
 songHtmlStr = str(songHtml.read())
 split - songHtmlStr.split('content by any third-party lyrics provider is prohibited by our license ...................................................')
 splitHtml = split[1]
 split = splitHtml.split('</div>', 1)
 lyrics = split[0]
 originalLyrics.write(lyrics)
 print(lyrics)
 originalLyrics.close()

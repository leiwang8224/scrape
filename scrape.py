import urllib2
from bs4 import BeautifulSoup

#specify url
quote_page = 'https://www.techiedelight.com/'

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib2.Request(quote_page, headers=hdr)

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(req)

# parse the html using the beautiful soap and store in var 'soup'
soup = BeautifulSoup(page, 'html.parser')

allTitles = soup.findAll('h2', attrs={'class':'entry-title'})

# get all links in the main webpage
allTitlesClean = []
for title in allTitles:
    titleBox = title.encode('utf-8')
    temp = (str.split(titleBox)[2])
    allTitlesClean.append(temp[6:-1])

# for each link goto it
for title in allTitlesClean:
    req2 = urllib2.Request(title, headers=hdr)
    page2 = urllib2.urlopen(req2)
    soup2 = BeautifulSoup(page2, 'html.parser')
    # get title
    # get problem description
    # get code
    # format to text file
    # add delay after each query

# open up the next page (2, 3, 4..)
# title_box = soup.find('h2', attrs={'class':'entry-title'}).encode('utf-8')
# title = str.split(title_box)[2]
# title = title[6:-1]
#
#
# page = urllib2.urlopen(urllib2.Request(title, header=hdr))



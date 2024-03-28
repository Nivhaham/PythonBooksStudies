import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def basicRequestGet():
    res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
    print(type(res))
    print(res.status_code == requests.codes.ok)
    print(len(res.text))
    print(res.text[:250])


# an example of how to handle a 404 error..
'''
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
'''


# writing the content of the get object to a text file. "chunk by chunk" 100000 bytes at a time.
'''
import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
'''

# Beautiful Soup is a python module designed for parsing html.



'''
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text) # returning a beautiful soup object 
'''

'''
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
'''

'''
soup.select('div') -  All elements named <div>
soup.select('#author') - The element with an id attribute of author
soup.select('.notice') - All elements that use a CSS class attribute
named notice
soup.select('div span') - All elements named <span> that are within
an element named <div>
soup.select('div > span') - All elements named <span> that are directly within an element named <div>,
with no other element in between
soup.select('input[name]') - All elements named <input> that have a
name attribute with any value
soup.select('input[type="button"]') - All elements named <input> that have an
'''

# selenium

'''The selenium module lets Python directly control the browser by programmatically
clicking links and filling in login information, almost as though
there is a human user interacting with the page. Selenium allows you to
interact with web pages in a much more advanced way than Requests and
Beautiful Soup; but because it launches a web browser, it is a bit slower and
hard to run in the background if, say, you just need to download some files
from the Web.'''

# sending special keys in selenium
'''
Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT - 
The keyboard arrow keys
Keys.ENTER, Keys.RETURN The enter and return keys Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP -
The home, end, pagedown, and pageup keys
Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE - 
The esc, backspace, and delete keys
Keys.F1, Keys.F2, . . . , Keys.F12 - The F1 to F12 keys at the top of the keyboard
Keys.TAB - The tab key
'''

#clicking browser buttons:
'''
browser.back() Clicks the Back button.
browser.forward() Clicks the Forward button.
browser.refresh() Clicks the Refresh/Reload button.
browser.quit() Clicks the Close Window button.
'''
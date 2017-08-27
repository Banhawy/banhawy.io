# Making a Python Web Crawler
Disclaimer: I am by no means an advanced developer/programmer now and I definitely didn't know python at all when I started my internship. Just because you might not know python or never automated anything with code before doesn't mean it will take you years to learn how to. In fact it only took me a week or so to get the hang of it.
![command line screenshot](../img/post2-0.png)
## The Problem: A manual daily task and a weak memory
Part of my job as a student intern developer is to provide occasional help to the marketing team in the office with analytics and data gathering.
One of those tasks is to check the university's main website's front page everyday to see if the featured article has changed. If so, I need to record the dates this article stayed up, take a screenshot, and record its title, description, and number of clicks it got in a google spreadsheet.

Those are A LOT of steps not to mention having to remember to do that every single day when I have so many other tasks. Also, what if I checked one day before leaving work at 5:00 PM, and the article was updated at 5:05PM. I would notice the change only next morning and record down the incorrect date of removal.

Up until 2 months ago, I did that routine and I was bad at it because some days I would forget to check and would have to check archive.org for a cached copy online. One day I decided I've had enough and decided to learn web crawling.

## Web Crawling with Python and Beautiful Soup:
Python is a really simple language that I managed to pick up in a week or two. You don't need to learn much except for the basic syntax, for loops, and importing libraries to start crawling the web. A good place to start is with this excellent book. (This links to the free online version)
In my case, I used a library called Beautiful Soup that basically takes an HTML page and breaks it down into one big dictionary you can traverse and change. If you want to learn more about how to use Beautiful Soup and go through a tutorial this post by Justin Yek is a great place to start.
I first created a python file, named it homepage, and imported the libraries to be used:
```
import datetime
import urllib2
from bs4 import BeautifulSoup
import unicodedata
```
I use the datetime library to record and print the date and time the crawler/program is run:
``` 
# Print Timestamp At time of crawl
datePosted = str(datetime.date.today())
print( 'Time of Crawl:  ' + datePosted)
```
I then use the urllib2 library to get the HTML document of the front page, and use BeautifulSoup library to parse it:
```
# Get page and parse its content
url =  'https://twin-cities.umn.edu/'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page,  'html.parser')
```
Now I have the page's HTML in a nice dictionary so I can extract the featured article's url, image link, title, and so on.
From inspecting the homepage in chrome dev tools, I find out that the featured article's image always has a class of either *mast__img* if it's a static image, or *mast__mobile* otherwise. (The otherwise happened when I found an error in the program's log one day not finding *mast__img*). I use BeatifulSoup's **.find()** method to target the article's image tag by its class:
```
# In case the featured article has an image
imageLinkText = soup.find( 'img', attrs={ 'class':  'mast__img'})
# In case the featured article has a video
videoLinkText = soup.find('img', attrs={'class': 'mast__mobile'})
```
Now the article's img tag is stored as an object in *imageLinkText/ videoLinkText*. Because I'm super lazy and I don't want to take a screenshot of the featured article as well, I will instead get the article's image link so I can access it even when a newer article is published. I use a similar technique to get that info, this time by targetting the image's src attribute:
```
# Get Image link
try:
   src = imageLinkText.get('src')
except AttributeError:
   src = videoLinkText.get('src')
imageLink = unicodedata.normalize('NFKD', src).encode('ascii', 'ignore')
print('Image Link: \n' + imageLink)
```
I need to normalize unicode data in src variable to remove umlauts, accents etc. For example "na&#239;ve caf&#233;	" would be changed to "naive cafe". I take this step to avoid any errors while printing out and storing ascii values.
![screenshot of website's source page](../img/post2-1.png)

Now to get the Article title and description I had to dig deep and be extra specific.
I can't use **.find()** to get the class *mast__text* because that would return both the article title in the first p child as well as the description in the second p child. Instead I used BeautifulSoup's CSS selector method **.select()** which takes css selectors as its argument. In my case, I want the first p child of the class *.mast__text* so I choose **".mast__text p:nth-of-type(1)"**:
```
# Get Article Title
articleTitle = soup.select('.mast__text p:nth-of-type(1)')[0].text.strip().encode('ascii', 'ignore').strip()
print(title)
```
This will return an array of the matching elements. If the selector is specific enough it should return an array with one item. I convert the item from html code to text with **.text** and strip away white spaces with **.strip()** and store it in articleTitle variable.
I use the same technique to get the article description:
```
# Get Article description
articleDescriptionList = soup.select('.mast__text p:nth-of-type(2)')
articleDescription = articleDescriptionList[0].text.strip().encode('ascii', 'ignore').strip()
print('Article Description: \n' + articleDescription)
```
Finally, I have the article link left to extract. Again I will use the css selector to get the first anchor tag within the featured article div given the class name *.node-promoted*:
```
# Get Article Link
articleLink = soup.select('.node-promoted a:nth-of-type(1)')
articleLink = articleLink[0].get('href')
print('Article Link: \n' + articleLink)
```
*soup.select( '.node-promoted a:nth-of-type(1)')* returns an array with first item as an html object:
``` 
<a href="https://twin-cities.umn.edu/news-events/creating-countrys-identity" title="Learn more about Haider's art.">
``` 

To get the article's url I use **.get()** to get the value within the href attribute.
Putting things together, the code should look like this:
```
import datetime
import urllib2
from bs4 import BeautifulSoup
import unicodedata

# Print Timestamp At time of crawl
datePosted = str(datetime.date.today())
print( 'Time of Crawl:  ' + datePosted)

# Get page and parse its content
url =  'https://twin-cities.umn.edu/'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page,  'html.parser')

# In case the featured article has an image
imageLinkText = soup.find( 'img', attrs={ 'class':  'mast__img'})
# In case the featured article has a video
videoLinkText = soup.find('img', attrs={'class': 'mast__mobile'})

# Get Image link
try:
   src = imageLinkText.get('src')
except AttributeError:
   src = videoLinkText.get('src')
imageLink = unicodedata.normalize('NFKD', src).encode('ascii', 'ignore')
print('Image Link: \n' + imageLink)

# Get Article Title
articleTitle = soup.select('.mast__text p:nth-of-type(1)')[0].text.strip().encode('ascii', 'ignore').strip()
print(title)

# Get Article description
articleDescriptionList = soup.select('.mast__text p:nth-of-type(2)')
articleDescription = articleDescriptionList[0].text.strip().encode('ascii', 'ignore').strip()
print('Article Description: \n' + articleDescription)

# Get Article Link
articleLink = soup.select('.node-promoted a:nth-of-type(1)')
articleLink = articleLink[0].get('href')
print('Article Link: \n' + articleLink)
```
The output when run from the command line should look like this:
![command line screenshot](../img/post2-2.png)

Voila! That's the first useful web crawler I wrote and I depend on it till today. Of course the first version wasn't perfect, and the try/catch blocks are the results of uncaught errors some days, and even when writing this post I managed to optimize it a bit more.

This program alone would have been enough for me to cut the time I spent on this task from 10-15 minutes to 3-5 minutes when using the crawler. That's what I did for a few days until I gave the program more features and hooked it up to a google spreadsheet to keep a log online. However, this is a topic for a later post.
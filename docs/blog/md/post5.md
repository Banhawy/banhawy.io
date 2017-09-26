# Crawling for RegEx with Python

## The Challenge:
Today at work I got an unexpected task from my marketing collegue to use a web crawler written by a developer who doesn't work with us anymore. The program was an old piece of ruby that runs on the terminal and takes a list of URLs as arguements. It would then scan those URLs for straight quotes (**'**) and return the URL and the Paragraph the quotes are present.

Sadly, the ruby program did not work (after spending 30 minutes setting up the correct development environment on my machine) because it did not account for **https** schemas and got denied by our website's servers. I did not bother reverse engineering it because I am not very familiar with ruby gems/libraries and I wanted to finish this task fairly quicky to move on to others on my list. So I decided to give it a go with python.

## The Solution:
Python is my to-go-to language when it comes to web crawling. I decidedto give python 3 a go so I can gradually transition into its syntax and libraries, which it turn out are very similar. 
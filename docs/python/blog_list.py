import blog_object
import blog
import blogpost
import os

personal_story = blog_object.Blog('My Developer Journey', 'A personal story about how I chose to become a developer', 'general', 'img/self.png', 'blog/My Developer Journey.html')
post2 = blog_object.Blog('3 Ways to Create React Components', 'A brief indtoduction on how to write components in React', 'javascript', 'img/reactjs.png', 'blog/3 Ways to Create React Components.html')
post3 = blog_object.Blog('Making a Python Web Crawler', 'How I made a Python Web Crawler to automate a boring daily task', 'python', 'img/post2-0.png', 'blog/Making a Python Web Crawler.html')
post5 = blog_object.Blog('Parsing Command Line Arguments in Python', 'Using python to read input and flags from the command line', 'python', 'img/post5.png', 'blog/Parsing Command Line Arguments in Python.html')
post6 = blog_object.Blog('Switching to HTTPS for Sites Hosted on AWS', 'How to register SSL Certificate on AWS', 'aws devops', 'img/post6.png', 'blog/Switching to HTTPS for Sites Hosted on AWS.html')
blog_list = [personal_story, post2, post3, post5, post6]

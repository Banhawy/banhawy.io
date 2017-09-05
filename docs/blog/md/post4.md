# Coding a Blog with Markdown, Python and Javascript

## The Challenge:
I like blogging about my personal projects. It helps reinforce my learning and sometimes helps guid others with theirs. I also like writing in *markdown* which is the syntax used in github pages. A few months ago I could have simply used github pages to accomplish that task, but I have my own domain and server now so that's not an option. I have been using **[medium](https://medium.com/@the.benhawy)** to write my blogposts. It's a great platform with a large audience, but I really despise the fact that it does not support markdown format as of yet. 

The idea I have in mind is that I would write my blogs offline in markdown once, save them in a repo on github, and be able to share and upload it anywhere that supports markdown. So I decided to build my own solution from scratch. 

## The Solution
I decided to use a compination of **python** and **javascript** to automate my blogging process. The end result would be me writing a markdown file, referencing the name, path, and metadata of that file in a python script which injects it into an html blog template that uses javascript to compile markdown into html, and css to apply github's markdown stylings to the page.

### Step 1: Write a Python Blog Class
This is a relatively simple step. I created a file called *blog_object.py* with a class called **Blog** that would be used in other python files to create an object that stores information about the blogpost. The information I'm interested in are: title, description, topic, image, and url.

The code looks like this:
```
class Blog():
    """ This class provides a way of storing project related information"""
    def __init__(self, title, description, topic, image, url):
        self.title = title
        self.description = description
        self.image_path = image
        self.topic = topic
        self.url = url
```
### Step 2: Write a Python file that creates Blogpost objects
In this step, I create a file called *blog_list.py* in which I create a *Blog* object for each post I write.  
```
import blog_object

post1 = blog_object.Blog('My Developer Journey', 'A personal story about how I chose to become a developer', 
'general', 'img/self.png', 'blog/My Developer Journey.html')
```
For example, after importing the blog_object file in which I declared the Blog class, I create a blog object for my first post stored in the variable *post1*. This object takes 5 parameters that I defined in the Blog class, such as *title, description, topic, etc.*  

****Note:** the **image** parameter takes in a path to an image in my website's file structure that will later be used as a thumbnail in blog listings. Similarly, the **url** parameter takes in the path to the html file of the blogpost which I'll discuss how it would be generated later on.
```
blog_list = [personal_story, post2, post3]

blog.open_blog(blog_list)
```
Next I create a list/array of blog posts called
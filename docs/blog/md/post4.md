# Parsing Command Line Arguments in Python


Python is a very flexible and popular programming language because of its simplicity, modularity, and power. So far I've been writing python programs that just automated some manual tasks and other statistical analysis work. However, I never really thought about running a python program with an arguement. The most I've interacted with a python program was just testing I/O methods while I was learning it.

This was until I was given a task at work that required me to write a reusable command line program that would take a URL and crawl that URL or the URL's entire domain and log the results based on the command line flags.

## The command line ARGS! (arguements)
Having your program accept arguements and flags on launch is a neat process. It's certainly the first time I have to program code like that in python (I've done it in node.js but not with flags). After considering my options when it comes to the python library I chose to go with **[argparse](https://docs.python.org/2/library/argparse.htm)**.

First I import the *argparse* library and I define an *ArgumentParser* object that will contain the neccessary information to parse the command line into Python data types. You can think of the ArguementParser object as an empty key/value dictionary.

```
#!/usr/local/bin/python3
import sys, argparse
import root_crawl, man_crawl

parser = argparse.ArgumentParser()
```

Now that I have a parser object, I need to fill it with arguements from the command lines. This is done by the *add_arguement()* method which when called on the parser object creates attributes in the parse with the values of the *add_argument* method.

```
parser.add_argument('url', help="Check a url for straight quotes", type=str)

args = parser.parse_args()
```
The above code tells the parser to take the first command line arguement, call it *url*, assume it is a string type, and provide custom help message about the argument variable when called with the -h/--help flag.

## Putting up the Flags
Now that I've created a place to store and parse my program's *1st* argument, I want to have additional optional flags to indicate whether the user wants to crawl a *specific page* or an *entire domain*.  

The two options I want are:
1. The ability to provide the website's root/main page and crawl the entire website.
2. The option to log the results into a spreadhseet.

For the first option I can create a flag, called *--root* or *-r* for short. 
For the second option I can create a flag, called *--excel* or *-e* for short.

How do we program this?

We use the same *add_argument()* method again to create these options with slightly different attributes.

```
parser.add_argument('url', help="Check a url for straight quotes", type=str)

parser.add_argument("-r", "--root", help="Scans all links on website's sitemap", action="store_true")

parser.add_argument("-e", "--excel", help="Logs results into an excel spreadsheet", action="store_true")

args = parser.parse_args()
```

When creating a flag, we need to provide the add_argument method with the name of the flag preceeded by the **--** or *-* prefix. (Note: It is not necessary to have both the short and long flag names, but it is preffered). The help attributes is useful to provide the user info about the flags, and the *action* attribute stores the boolean value *True*. 

Notice that we haven't touched on the subject of crawling which is discussed in a separate blog post.

## Implementing the Logic

Now that we have the positional arguement and the optional flags defined, it's time to implement the logic of the program.

First we start off with the basecase. The simplest way a user would use the program is to to call the program and provide it with just one URL to crawl.
```
python3 scan URL
```
In this case the program will take the first command line arguement *URL* and match it against the ArgParse parser object's attributes. It will store the URL given in the command line in the first non-flag attribute *url* of the parser object.

What about the other attributes of the parser object, namely --root and --excel?

They default to *False*.
To see this inaction you can print out the parser object *args* to screen to get the following:
```
$ python3 scan.py  https://www.google.com

=>$ Namespace(excel=False, root=False, url='https://www.google.com')
``` 
To access and use the URL in the first command line arguement we can use **args.url**

In my case, I will pass the url and the truth value of the excel flag to to a function that will crawl the webpage and log the results to a spreadsheet if the excel value is True. This function is defined in a separate file so I import and use it.

```
man_crawl.crawl(args.url, args.excel)
```
Now any website put as the first command line arguement will be passed as the first parameter of the crawler function. I also pass the excel attribute of the parser object which defaults to false because the *-e/--excel* flag was not used in the command line. If the user were to use the *--excel* flag then *args.excel* would be set to *True*.

The other case is if the user uses the *-r/--root* flag to indicate the intention to crawl the entire website. In this case we need to modify the code to check first if the root flag was used:
```
if args.root:
    root_crawl.crawl(args.url, args.excel)
else:
    man_crawl.crawl(args.url, args.excel)
``` 
Of course, if the root flag is used then it would use another function from another file that I import as well.

Best thing about the *argparse* module is that it automatically handles the **-h/--help** flag that pulls all those flag help info written earlier and displays them nicely on the command line.

```
$ python3 scan.py -h
usage: scan.py [-h] [-r] [-e] url

positional arguments:
  url          Check a url for straight quotes

optional arguments:
  -h, --help   Show this help message and exit
  -r, --root   Scans all links on website's sitemap
  -e, --excel  Logs results into an excel spreadsheet
```

In the end the code should look like this:
```
#!/usr/local/bin/python3
import argparse
import root_crawl, man_crawl

parser = argparse.ArgumentParser()
parser.add_argument('url', help="Check a url for straight quotes", type=str)
parser.add_argument("-r", "--root", help="Scans all links on website's sitemap", action="store_true")
parser.add_argument("-e", "--excel", help="Logs results into an excel spreadsheet", action="store_true")

args = parser.parse_args()

if args.root:
    root_crawl.crawl(args.url, args.excel)
else:
    man_crawl.crawl(args.url, args.excel)
```

Of course, this interaction could be implemnted differently using I/O but it just so happens that this was the requirement, and for UNIX and terminal users this should be very user friendly and efficient.
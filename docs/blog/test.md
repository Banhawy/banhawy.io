# Classic Tomatoes

Classic Tomatoes is a website built with python that displays a list of movies or TV shows on a single page as clickable tiles. Clicking a movie would show you some info and automatically plays a youtube trailer of that movie. 

[View Demo](https://banhawy.github.io/Classic_Tomatoes/)


### Installation

This app was developed and tested with [python 2.7.10](https://www.python.org/downloads/release/python-2710/). Python _must_ be installed to build the website.

Installing and running Classic Tomatoes is very simple and can be done in 3 steps:
1. Clone or fork  the github repository
2. cd into the _Classic_Tomatoes_ directory on your machine
3.Use python to run the script `entertainment_center.py`

```sh
$ cd Classic_Tomatoes
$ python entertainment_center.py
```

That's it! 
A webbrowser should be launched and it should display a Classic Tomatoes website template.

### Usage

If you want to custumize the movies displaying on the web page, you can do so by editing the `entertainment_center.py` file. 

To **add/remove** a movie from web page, edit the `movie_list` list variable to include your desired movie selection. Then run `python entertainment_center.py` again to see your changes.

##### ****Note*
If one or more movies you entered in the list does not have a trailer link in the database, the terminal will display a message indicating which movie(s) needs their trailers entered manually. You can do so in the rendered html document. A placeholder 'Coming Soon' video will be placed on the webpage until you do so.

### Todos

 - Add tile animations 
 - Add TV shows section
 
###### This project is based on original starter code by [adarsh0806](https://github.com/adarsh0806/ud036_StarterCode)

License
----

MIT
import project_object
import portfolio

bulletin_description = '''This is a virtual bulletin board one-page application built with React. 
It's my first project learning React. Used React components, ES6 syntax, and React production environment.'''

classic_tomatoes_description = '''This is a single page web app built entirely with python code. Used movie APIs
and some jQuery and bootstrap. It is easily customizable and can genrate a movie library with trailers and info 
by just inserting movie title names in a python list. '''

drumpfinator_description = '''A chrome extension written in Javascript that automatically detects and replaces
any text instances of "Trump" with "Drumpf" and changes any images with description of Trump into a random image/gif of Obama instead. 
Will use neural networks and deep learnig for facial recognition in future versions.'''

weather_description = '''This is my first project working with APIs. The web app fetches the user's geolocation and calls an API to display
the weather data of that location. The background image also changes (via Flikr API) based on the user's location or entered city query. 
'''
rqg_description = '''This is a a web app that generates random quotes from different world leader. I wrote the JSON API that serves the app
 myself and fetched it via ajax. The app changes the background and displays a portrait of the leader with a link to his/her wiki page and a tweet button.'''

wiki_description = '''A SPA that takes user input and queries Wikipedia for a given term. Results are formatted and listed after asynchronous call is made. 
                     This project is built with React, JSX, and Material-UI. '''

bulletin_board = project_object.Project('Bulletin Board', bulletin_description, 
                                            'img/bulletin.png', 'https://banhawy.github.io/Bulletin-Board/')

classic_tomatoes = project_object.Project('Classic Tomatoes', classic_tomatoes_description, 
                                            'img/classicT.png', 'https://banhawy.github.io/Classic_Tomatoes/')

drumpfinator = project_object.Project('Make Donald Drumpf Again', drumpfinator_description, 
                                        'img/extension.png', 'https://chrome.google.com/webstore/detail/make-donald-drumpf-again/eppfpfolmpkpclmcpgplmfllbnokngbb?hl=en-US')

weather_machine = project_object.Project('The Weather Machine', weather_description, 'img/weather.png',
                                    'https://banhawy.github.io/LocalWeather')

quote_generator = project_object.Project('Random Quote Generator', rqg_description, 'img/rqg.png', 'https://codepen.io/Banhawy/full/rWZxMv/')

wiki_viewer = project_object.Project('Wikipedia Viewer', wiki_description, 'img/wiki.png', 'https://banhawy.github.io/Wikipedia-Viewer/')

portfolio_projects = [ wiki_viewer, bulletin_board, classic_tomatoes, drumpfinator, weather_machine, quote_generator ]

portfolio.open_portfolio(portfolio_projects)
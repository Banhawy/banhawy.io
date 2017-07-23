import project_object
import portfolio

bulletin_description = '''This is a virtual bulletin board one-page application built with React. 
It's my first project learning React. Used React components, ES6 syntax, and React production environment.'''

classic_tomatoes_description = '''This is a single page web app built entirely with python code. Used movie APIs
and some jQuery and bootstrap. It is easily customizable and can genrate a movie library with trailers and info 
by just inserting movie title names in a python list. '''

drumpfinator_description = '''This is a chrome extension written in Javascript that automatically detects and replaces
any text instances of "Trump" with "Drumpf" and changes any images with description of Trump into a random image/gif of Obama instead. 
Although a fun side project, it is a good ongoing experience with DOM manipulation and a good candidate for practicing nearal networks
and deep learning to detect Trump photos instead of relying on image descriptions.'''

bulletin_board = project_object.Project('Bulletin Board App', bulletin_description, 
                                            'img/bulletin.png', 'https://banhawy.github.io/Bulletin-Board/')

classic_tomatoes = project_object.Project('Classic Tomatoes', classic_tomatoes_description, 
                                            'img/classicT.png', 'https://github.com/Banhawy/Classic_Tomatoes')

drumpfinator = project_object.Project('Make Donald Drumpf Again', drumpfinator_description, 
                                        'img/extension.png', 'https://chrome.google.com/webstore/detail/make-donald-drumpf-again/eppfpfolmpkpclmcpgplmfllbnokngbb?hl=en-US')




portfolio_projects = [ bulletin_board, classic_tomatoes, drumpfinator ]

portfolio.open_portfolio(portfolio_projects)
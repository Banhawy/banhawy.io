import os
import re

main_content = '''<!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <!-- Bootstrap 3 -->
        <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
        <link rel="stylesheet" href="styles/css/styles.css">
        <!--Font Awesome-->
        <script src="https://use.fontawesome.com/80270d8f99.js"></script>

        <title>Adham's Blog</title>
    </head>
    <body>
        <!-- NAV BAR -->
        <nav>
            <div class="container">
                <ul class="nav-links">
                    <li><a href="index.html">ABOUT</a></li>
                    <li><a href="resume.html">RESUME</a></li>
                    <li><a href="portfolio.html">PORTFOLIO</a></li>
                    <li class="active"><a href="#">Blog</a></li>
                </ul>
                <div class="menu" onclick="openNav()">
                    <div class="bar"></div>
                    <div class="bar"></div>
                    <div class="bar"></div>
                </div>
            </div>
        </nav>
        <div id="mySidenav" class="sidenav">
            <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
            <a href="index.html">ABOUT</a>
            <a href="resume.html">RESUME</a>
            <a href="portfolio.html">PORTFOLIO</a>
            <a href="#">Blog</a>
        </div>

        <section id="blog" class="blogposts">
        <div class="button-group filter-button-group">
            <button data-filter="*">show all</button>
            <button data-filter=".metal">metal</button>
            <button data-filter=".transition">transition</button>
        </div>
            <div class="grid"'>
                <div class="grid-item">
                    <div class="card" style="width: 200px">
                        <img src="img/self.png" alt="Avatar" style="width:100%">
                        <div class="container">
                            <h4><b>John Doe</b></h4> 
                            <p>Architect & Engineer</p> 
                        </div>
                    </div>
                </div>
                <div class="grid-item metal">
                    <div class="card" style="width: 200px">
                        <img src="img/self.png" alt="Avatar" style="width:100%">
                        <div class="container">
                            <h4><b>John Doe</b></h4> 
                            <p>Architect & Engineer</p> 
                        </div>
                    </div>
                </div>
                <div class="grid-item">
                    <div class="card transition" style="width: 200px">
                        <img src="img/self.png" alt="Avatar" style="width:100%">
                        <div class="container">
                            <h4><b>John Doe</b></h4> 
                            <p>Architect & Engineer</p> 
                        </div>
                    </div>
                </div>
            
            </div>
        </section>
        <footer>
            <div class="container-fluid social-links">
                <div class="logos">
                    <div class="row">
                        <div class="col-xs-4">
                            <a href="https://github.com/Banhawy" target="_blank">
                                <img src="img/github-logo.png" alt="github link">
                            </a>
                        </div>
                        <div class="col-xs-4">
                            <a href="https://www.linkedin.com/in/adham-banhawy/" target="_blank">
                                <img src="img/linkedin-logo.png" alt="linkdin link">
                            </a>
                        </div>
                        <div class="col-xs-4">
                            <a href="https://twitter.com/adham_benhawy" target="_blank">
                                <img src="img/twitter-logo.png" alt="twitter link">
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="container-fluid footer">
                <div class="row">
                    <div class="col-xs-6">
                        <p>3131 Sumter Ave N, Crystal, 55427 MN</p>
                    </div>
                    <div class="col-xs-6">
                        <p id="email">the.benhawy@ gmail.com</p>
                    </div>
                </div>
            </div>
        </footer>
        <script src="js/jquery.min.js"></script>
        <script src="js/index.js"></script>
        <script src="js/isotope.min.js"></script>
        <script src="js/filter.js"></script>
        
    </body>

    </html>
'''

def open_blog(title):
    html_file = title + '.html'
    output_file = open(html_file, 'w')
    output_file.write(main_content)
    output_file.close()
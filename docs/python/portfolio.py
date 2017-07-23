import os
import re

main_content = '''
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <!-- Bootstrap 3 -->
        <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
        <link rel="stylesheet" href="styles/css/styles.css">
        <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
        <!--Font Awesome-->
        <script src="https://use.fontawesome.com/80270d8f99.js"></script>

        <title>Adham's Resume</title>
    </head>
    <body>
        <!-- NAV BAR -->
        <nav>
            <div class="container">
                <ul class="nav-links">
                    <li><a href="index.html">ABOUT</a></li>
                    <li><a href="resume.html">RESUME</a></li>
                    <li class="active"><a href="#">PORTFOLIO</a></li>
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
            <a href="#">PORTFOLIO</a>
        </div>

        <section id="main" class="projects">
            {project_sections}
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
    </body>

    </html>
'''

project_section_odd = '''
    <div class="container">
            <div class="row">
                <div class="col-sm-3 description">
                    <h3>{project_title}</h3>
                    <p>{project_description}</p>
                    <a href="{project_url}" target="_blank"><h4>View this project</h4></a>
                </div>
                <div class="col-sm-9">
                    <img src="{img_path}" alt="" />
                </div>
            </div>
        </div>
'''
project_section_even ='''
    <div class="container">
        <div class="row">
            <div class="col-lg-9">
                <img src="{img_path}" alt="" />
            </div>
            <div class="col-lg-3 description">
                <h3>{project_title}</h3>
                <p>{project_description}</p>
                <a href="{project_url}" target="_blank"><h4>View this project</h4></a>
            </div>
        </div>
    </div>
'''

def add_projects(projects):
    content = ''
    count = 3
    for project in projects:
        even = count%2 == 0
        if even:
            content += project_section_even.format(
            project_title=project.title,
            project_description=project.description,
            img_path=project.image_path,
            project_url=project.url
            ) 
        else:
            content += project_section_odd.format(
            project_title=project.title,
            project_description=project.description,
            img_path=project.image_path,
            project_url=project.url
            )
        count +=1
    return content

def open_portfolio(projects):
    output_file = open('portfolio.html', 'w')

    rendered_projects = main_content.format(
            project_sections=add_projects(projects)
        )
    output_file.write(rendered_projects)
    output_file.close()
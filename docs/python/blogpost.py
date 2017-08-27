import os
import re

header_content = '''<!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <!-- Bootstrap 3 -->
        <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
        <link rel="stylesheet" href="../styles/css/external/github-markdown.css">
        <link rel="stylesheet" href="../styles/css/styles.css">
        <!--Font Awesome-->
        <script src="https://use.fontawesome.com/80270d8f99.js"></script>
        <script src="../js/marked.js"></script>
        <style>
            .markdown-body {
                box-sizing: border-box;
                min-width: 200px;
                max-width: 980px;
                margin: 0 auto;
                padding: 45px;
            }

            @media (max-width: 767px) {
                .markdown-body {
                    padding: 15px;
                }
            }
        </style>
'''
main_content= ''' <title>{blog_title}</title>
    </head>
    <body>
        <!-- NAV BAR -->
        <nav>
            <div class="container">
                <ul class="nav-links">
                    <li><a href="../index.html">ABOUT</a></li>
                    <li><a href="../resume.html">RESUME</a></li>
                    <li><a href="../portfolio.html">PORTFOLIO</a></li>
                    <li class="active"><a href="../blog.html">BLOG</a></li>
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
            <a href="../index.html">ABOUT</a>
            <a href="../resume.html">RESUME</a>
            <a href="../portfolio.html">PORTFOLIO</a>
            <a href="../blog.html">BLOG</a>
        </div>
        <article id="content" class="markdown-body">
            
        </article>
        <footer>
            <div class="container-fluid social-links">
                <div class="logos">
                    <div class="row">
                        <div class="col-xs-4">
                            <a href="https://github.com/Banhawy" target="_blank">
                                <img src="../img/github-logo.png" alt="github link">
                            </a>
                        </div>
                        <div class="col-xs-4">
                            <a href="https://www.linkedin.com/in/adham-banhawy/" target="_blank">
                                <img src="../img/linkedin-logo.png" alt="linkdin link">
                            </a>
                        </div>
                        <div class="col-xs-4">
                            <a href="https://twitter.com/adham_benhawy" target="_blank">
                                <img src="../img/twitter-logo.png" alt="twitter link">
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
        <script src="../js/jquery.min.js"></script>
        <script src="../js/index.js"></script>
        <script>
            document.getElementById('content').innerHTML=marked(`<a href="../blog.html">Back to Blog</a><br> \n {blog_post}`);
        </script>
    </body>

    </html>
'''

def open_blog(title, content):
    html_file = title + '.html'
    path = os.path.join(os.path.dirname(__file__), '..', 'blog', html_file)
    output_file = open(path, 'w')
    rendered_blog = main_content.format(
        blog_title=title,
        blog_post=content
    )
    output_file.write(header_content + rendered_blog)
    output_file.close()
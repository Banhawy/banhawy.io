import blogpost
import os

path = os.path.join(os.path.dirname(__file__), '..', 'blog', 'test.md')
blog = open(path)
content = blog.read()
blog.close()
# '# Fucked in browser\n\nRendered by **marked**.'
blogpost.open_blog('Test Blog', content)
import blogpost
import os

path = os.path.join(os.path.dirname(__file__), '..', 'blog', 'test.md')
blog = open(path)
content = blog.read().replace('\n', '\\n').replace('`', '\`')
blog.close()

blogpost.open_blog('Test Blog', content)
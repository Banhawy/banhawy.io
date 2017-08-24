import blog_object
import blog
import blogpost
import os

path = os.path.join(os.path.dirname(__file__), '..', 'blog', 'test.md')
document = open(path)
content = document.read().replace('\n', '\\n').replace('`', '\`')
document.close()

blogpost.open_blog('Test Blog', content)

personal_story = blog_object.Blog('Personal Story', 'A personal story about how I chose to become a developer', 'general', 'img/self.png')
blog_list = [personal_story]

blog.open_blog(blog_list)
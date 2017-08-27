import blog_object
import blog
import blogpost
import os

path = os.path.join(os.path.dirname(__file__), '..', 'blog', 'md', 'post3.md')
document = open(path, encoding='utf8')
content = document.read().replace('\n', '\\n').replace('`', '\`').replace('</script', '<\/script').replace("'", "\'")
document.close()

blogpost.open_blog('Making a Python Web Crawler', content)

personal_story = blog_object.Blog('My Developer Journey', 'A personal story about how I chose to become a developer', 'general', 'img/self.png', 'blog/My Developer Journey.html')
post2 = blog_object.Blog('3 Ways to Create React Components', 'A brief indtoduction on how to write components in React', 'javascript', 'img/reactjs.png', 'blog/3 Ways to Create React Components.html')
post3 = blog_object.Blog('Making a Python Web Crawler', 'How I made a Python Web Crawler to automate a boring daily task', 'python', 'img/post2-0.png', 'blog/Making a Python Web Crawler.html')
blog_list = [personal_story, post2, post3]

blog.open_blog(blog_list)
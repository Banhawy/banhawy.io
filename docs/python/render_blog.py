import blog_list
#import blog_object
import blog
import blogpost
import os

blogs = blog_list.blog_list

for blog_post in blogs:
    post = 'post' + str(blogs.index(blog_post)+1) + '.md'
    path = os.path.join(os.path.dirname(__file__), '..', 'blog', 'md', post)
    document = open(path, encoding='utf8')
    content = document.read().replace('\n', '\\n').replace('`', '\`').replace('</script', '<\/script').replace("'", "\'")
    document.close()

    blogpost.open_blog(blog_post.title, content, blog_post.description)

blog.open_blog(blogs)
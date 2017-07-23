class Project():
    """ This class provides a way of storing project related information"""
    def __init__(self, title, description, image, link):
        self.title = title
        self.description = description
        self.image_path = image
        self.url = link

    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description

    def get_image(self):
        return self.image_path
    
    def set_url(self, link):
        self.url=link
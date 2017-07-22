class Project():
    """ This class provides a way of storing project related information"""
    def __init__(self, title, description, image_path, footer):
        self.title = title
        self.description = description
        self.image_path = image_path
        self.footer = footer

    def title(self):
        return self.title
    
    def description(self):
        return self.description

    def image(self):
        return self.image_path
    
    def footer(self):
        return self.footer
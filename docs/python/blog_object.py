class Blog():
    """ This class provides a way of storing project related information"""
    def __init__(self, title, description, topic, image):
        self.title = title
        self.description = description
        self.image_path = image
        self.topic = topic
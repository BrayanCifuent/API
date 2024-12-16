# modelos/modelos.py

class Usuario:
    def __init__(self, id, name, email, username, phone, website):
        self.id = id
        self.name = name
        self.email = email
        self.username = username
        self.phone = phone
        self.website = website

class Post:
    def __init__(self, id, user_id, title, body):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.body = body

class Comment:
    def __init__(self, id, post_id, name, email, body):
        self.id = id
        self.post_id = post_id
        self.name = name
        self.email = email
        self.body = body

class Album:
    def __init__(self, id, user_id, title):
        self.id = id
        self.user_id = user_id
        self.title = title

class Photo:
    def __init__(self, id, album_id, title, url):
        self.id = id
        self.album_id = album_id
        self.title = title
        self.url = url

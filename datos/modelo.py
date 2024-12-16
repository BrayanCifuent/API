class Usuario:
    def __init__(self, id, name, username, email):
        self.id = id
        self.name = name
        self.username = username
        self.email = email

class Post:
    def __init__(self, id, user_id, title, body):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.body = body

class Album:
    def __init__(self, id, user_id, title):
        self.id = id
        self.user_id = user_id
        self.title = title

class Comentario:
    def __init__(self, id, post_id, name, email, body):
        self.id = id
        self.post_id = post_id
        self.name = name
        self.email = email
        self.body = body
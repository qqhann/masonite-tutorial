""" Post Model """

from orator.orm import belongs_to

from config.database import Model


class Post(Model):
    """Post Model
    """

    __fillable__ = ['title', 'author_id', 'body']

    @belongs_to('author_id', 'id')
    def author(self):
        from app.User import User
        return User

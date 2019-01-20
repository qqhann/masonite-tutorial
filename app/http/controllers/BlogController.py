""" A BlogController Module """

from masonite.request import Request
from masonite.view import View

from app.Post import Post


class BlogController:
    """BlogController
    """

    def show(self, view: View):
        return view.render('blog')

    def store(self, request: Request):
        Post.create(
            title=request.input('title'),
            body=request.input('body'),
            author_id=request.user().id,
        )
        return 'post created'
